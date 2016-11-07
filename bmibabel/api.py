#! /usr/bin/env python
"""Work with api.yaml files from a BMI description."""

import os

import yaml
import pkgconfig

from .utils import cd, check_output
from .errors import (ParseError, MissingKeyError, UnknownKeyError,
                     MissingFileError)
# from . import build
from .utils import read_first_of


_API_FILES = [os.path.join('.bmi', 'api.yaml'),
              os.path.join('.bmi', 'api.yml')]

_REQUIRED_KEYS = set(['language', ])
_OPTIONAL_KEYS = set(['name', 'type', 'register', 'class', 'package',
                      'libs', 'cflags', 'includes', 'build', 'path',
                      'initialize_args'])
_VALID_KEYS = _REQUIRED_KEYS | _OPTIONAL_KEYS


def validate_api(api):
    """Validate API description or raise an exception.

    Parameters
    ----------
    api : dict_like
        Description of a BMI.

    Raises
    ------
    ParseError
        If the description object is invalid.
    MissingKeyError
        If a required key is missing
    UnknownKeyError
        If an unknown key is found
    """
    if not isinstance(api, dict):
        raise ParseError('object is not a dictionary')

    found_keys = set(api.keys())

    if not found_keys.issuperset(_REQUIRED_KEYS):
        raise MissingKeyError(_REQUIRED_KEYS - found_keys)

    if not found_keys.issubset(_VALID_KEYS):
        raise UnknownKeyError(found_keys - _VALID_KEYS)

    return True


def prepend_env_path(path_var, path, env=None):
    """Prepend a path to and environment variable.

    Parameters
    ----------
    path_var : str
        Environment variable.
    path : str
        Path to prepend.
    env : dict, optional
        Environment to use, otherwise the current environment.
    """
    env = env or os.environ

    try:
        if path not in env[path_var]:
            env[path_var] = os.pathsep.join([path, env[path_var]])
    except KeyError:
        env[path_var] = path


def pkg_config(package, opt):
    """Use pkg-config to get compile options.

    Parameters
    ----------
    package : str
        Name of pkg-config package.
    opt : {'--cflags', '--libs'}
        Options for pkg-config.

    Returns
    -------
    str
        Compiler flags.
    """
    import copy

    assert(opt in ['--cflags', '--libs'])

    env = copy.copy(os.environ)
    if 'CSDMS_PREFIX' in env:
        pkg_config_path = os.path.join(env['CSDMS_PREFIX'], 'lib', 'pkgconfig')
        prepend_env_path('PKG_CONFIG_PATH', pkg_config_path, env=env)

    return check_output(['pkg-config', opt, package], env=env).strip()


def find_api_description_file(dir='.'):
    with cd(dir):
        (_, contents) = read_first_of(['.bmi.yaml', '.bmi.yml'])
        desc = yaml.load(contents)
        if 'implementation' in desc:
            if isinstance(desc['implementation'], dict):
                return desc['implementation']


_POSSIBLE_API_NAMES = [
    os.path.join('.bmi', 'api.yaml'),
    os.path.join('.bmi', 'api.yml'),
    'api.yaml',
    'api.yml',
]


def load_api(fname):
    if os.path.isfile(fname):
        path_to_bmi = os.path.dirname(fname)
    else:
        path_to_bmi = fname

    with cd(path_to_bmi):
        (path_to_api, contents) = read_first_of(_POSSIBLE_API_NAMES)
        api = yaml.load(contents)
        api['path'] = os.path.dirname(path_to_api)

    validate_api(api)

    return api


def load(dir='.'):
    """Load an api description from a file.

    Parameters
    ----------
    dir : str, optional
        Path to folder that contains description file.

    Returns
    -------
    dict
        Description of the API.

    Raises
    ------
    ParseError
    MissingKeyError
    UnknownKeyError
        If the description is invalid.
    MissingFileError
        If an api file cannot be read.
    """
    with cd(dir):
        (path_to_api, contents) = read_first_of(
            [os.path.join('.bmi', 'api.yaml'),
             os.path.join('.bmi', 'api.yml'), 'api.yaml', 'api.yml'])
        api = yaml.load(contents)
        api['path'] = os.path.dirname(path_to_api)

    validate_api(api)

    api.pop('build', None)

    if api['language'] in ('c', 'cxx'):
        cflags = api['cflags']
        if isinstance(cflags, dict) and 'pkgconfig' in cflags:
            api['cflags'] = pkgconfig.cflags(cflags['pkgconfig'])

        libs = api['libs']
        if isinstance(libs, dict) and 'pkgconfig' in libs:
            api['libs'] = pkgconfig.libs(libs['pkgconfig'])
    elif api['language'] == 'python':
        pass

    return api


def load_all(dir='.'):
    """Load multiple API descriptions.

    Parameters
    ----------
    dir : str, optional
        Path to folder that contains description file.

    Returns
    -------
    list
        Descriptions of APIs.
    """
    with cd(dir):
        try:
            (_, contents) = read_first_of(['.bmi.yaml', '.bmi.yml'])
        except MissingFileError:
            apis = [load()]
        else:
            bmi = yaml.load(contents)
            apis = [load(dir=path) for path in bmi['bmi_paths']]

    return apis


def get_subdirs(dir='.'):
    return next(os.walk(os.path.join(dir)))[1]


def is_bmi_metadata_folder(path):
    try:
        with open(os.path.join(path, 'api.yaml'), 'r') as fp:
            yaml.load(fp)
    except IOError, yaml.error.YAMLError:
        return False
    else:
        return True


def find_bmi_metadata(dir='.'):
    """Find BMI metadata in a directory tree.

    A folder is thought to contain BMI metadata if:

    *  Its name is `.bmi` and contains a `api.yaml`. If it contains only
       folders, each folder is assumed to contain bmi metadata for an
       individual model.
    *  It is listed in `.bmi.yaml` file under `bmi_paths`. If any of these
       paths do not end in `.bmi`, but there is a `.bmi` folder there, that
       folder is used.

    Parameters
    ----------
    dir : str, optional
        Path to folder to search for metadata.

    Returns
    -------
    tuple of str
        Paths to BMI metadata folders.
    """
    found = set()

    if not os.path.isdir(dir):
        raise ValueError('{dir}: not a directory'.format(dir=dir))

    for root, dirs, files in os.walk(dir):
        paths = []

        if '.bmi' in dirs:
            paths.append('.bmi')
            paths.extend(get_subdirs(os.path.join(root, '.bmi')))

        for fname in ('.bmi.yaml', '.bmi.yml'):
            try:
                bmi_paths = load_bmi_paths(fname, dir=root)
            except IOError:
                pass
            except yaml.error.YAMLError:
                pass
            else:
                paths.extend(bmi_paths)

        for path in paths:
            found.add(os.path.normpath(os.path.join(root, path)))

    for path in tuple(found):
        if not is_bmi_metadata_folder(path):
            found.remove(path)

    return tuple(found)


def load_bmi_paths(fname, dir='.'):
    paths = []
    with cd(dir):
        with open(fname, 'r') as fp:
            bmi = yaml.load(fp)

        for bmi_path in bmi.get('bmi_paths', []):
            if os.path.isdir(bmi_path):
                if os.path.isdir(os.path.join(bmi_path, '.bmi')):
                    bmi_path = os.path.join(bmi_path, '.bmi')
                paths.append(bmi_path)

    return paths
