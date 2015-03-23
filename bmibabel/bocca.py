#! /usr/bin/env python
"""Some bocca utilities."""

import os
import subprocess
import types
import re
import fileinput
import shutil
import glob
from string import Template

import yaml
from distutils.dir_util import mkpath

from .utils import cd, mktemp, which, system, check_output


_THIS_DIR = os.path.dirname(__file__)
_PATH_TO_IMPL = {
    'c': os.path.join(_THIS_DIR, 'data', 'c.Component'),
    'cxx': os.path.join(_THIS_DIR, 'data', 'csdms.examples.cxx.Heat'),
    'f90': os.path.join(_THIS_DIR, 'data', 'csdms.examples.f90.Heat'),
    'python': os.path.join(_THIS_DIR, 'data', 'py.Component'),
}

_PATH_TO_SIDL = os.path.join(_THIS_DIR, 'data')


class Error(Exception):

    """Base exception class for this module."""

    pass


class ProjectExistsError(Error):

    """Raise this exception for an already existing project."""

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Bocca(object):

    """Build babel projects with bocca."""

    def __init__(self, bocca=None):
        self._bocca = bocca or which('bocca')
        if self._bocca is None:
            raise RuntimeError('unable to find bocca')

    @property
    def bocca(self):
        """Path to bocca command."""
        return self._bocca

    def create_project(self, name, language=None, ifexists='raise'):
        """Create a new bocca project.

        Parameters
        ----------
        name : str
            Name of the new bocca project.
        language : str, optional
            Default language for the project.
        ifexists : {'pass', 'raise', 'clobber'}
            What to do if the project already exists.
        """
        if ifexists not in ['pass', 'raise', 'clobber']:
            raise ValueError('ifexists value not understood')

        options = []
        if language is not None:
            options += ['--language=%s' % language]

        if is_bocca_project(name):
            if ifexists == 'raise':
                raise ProjectExistsError('project exists')
            elif ifexists == 'clobber':
                shutil.rmtree(name)

        system([self.bocca, 'create', 'project', name] + options)

    def create_interface(self, name, sidl=None):
        """Create a new interface.

        Parameters
        ----------
        name : str
            Name of the new interface.
        sidl : str, optional
            Path to a SIDL description of the interface.
        """
        if sidl is None or sidl is True:
            sidl = os.path.join(_PATH_TO_SIDL, name + '.sidl')

        options = []
        if isinstance(sidl, types.StringTypes):
            options += ['--import-sidl=%s@%s' % (name, sidl)]

        system([self.bocca, 'create', 'interface', name] + options)


    def create_class(self, name, implements=None, language=None, sidl=None,
                     impl=None):
        """Create a new class.

        Parameters
        ----------
        name : str
            Name of the new interface.
        implements : str, optional
            Name of a babel interface the class implements.
        language : {'c', 'cxx', 'python'}
            Language of the class implementation.
        sidl : str, optional
            Path to a SIDL description of the interface.
        impl : str, optional
            Path to folder containing implementation files to import.
        """
        options = []
        if sidl is not None:
            options += ['--import-sidl=%s@%s' % (name, sidl)]
        if impl is not None:
            options += ['--import-impl=%s@%s' % (name, impl)]
        if language is not None:
            options += ['--language=%s' % language]
        if implements is not None:
            options += ['--implements=%s' % implements]

        system([self.bocca, 'create', 'class', name] + options)

        if impl:
            for fname in ['make.vars.user', 'make.rules.user']:
                shutil.copy(os.path.join(impl, fname),
                            os.path.join('components', name))

    def create_bmi_class(self, name, language='c', bmi_mapping=None,
                         pkg_config_package=None, impl=None):
        """Create a class that implements the Basic Model Interface.

        Parameters
        ----------
        name : str
            Name of the new interface.
        bmi_mapping : dict_like
            Substitutions to make in the implementation files.
        pkg_config_package : str
            Name of a pkg-config package.
        language : {'c', 'cxx', 'python'}
            Language of the class implementation.
        impl : str, optional
            Path to folder containing implementation files to import.
        """
        bmi_mapping = bmi_mapping or {}

        kwds = dict(implements='csdms.core.Bmi', language=language)
        if impl is None:
            self.create_class(name, **kwds)
        else:
            with mktemp(prefix='csdms', suffix='.d') as destdir:
                kwds['impl'] = make_impl_dir(name, language, subs=bmi_mapping)
                self.create_class(name, **kwds)


def make_impl_dir(name, language, subs=None, destdir='.'):
    """Create a folder with implementation code.

    Parameters
    ----------
    name : str
        Name of the new component class.
    language : {'c', 'cxx', 'python'}
        Language of the new class.
    subs : dict, optional
        Substitutions to make in the impl files.
    destdir : path, optional
        Path to folder that will contain new impl files.

    Returns
    -------
    str
        Path to new impl folder.
    """
    subs = subs or {}

    src_impls = _PATH_TO_IMPL[language]

    impl_dir = dup_impl_files(src_impls, name, destdir=destdir,
                              language=language)
    replace_bmi_names(glob.glob(os.path.join(impl_dir, '*')), subs)

    return impl_dir


def is_bocca_project(name):
    """Check if a folder is a bocca project.

    Parameters
    ----------
    name : str
        Name of folder.

    Returns
    -------
    boolean
        ``True`` if the folder contains a bocca project. Otherwise, ``False``.
    """
    return os.path.isdir(os.path.join(name, 'BOCCA'))


def class_language(name, bocca=None):
    """Get the language of a class within a bocca project.

    Parameters
    ----------
    name : str
        Name of class.
    bocca : str, optional
        Path to the bocca program.

    Returns
    -------
    str
        Language of the class.
    """
    bocca = bocca or which('bocca')

    import re

    lines = check_output([bocca, 'display', 'class', name]).split(os.linesep)
    m = re.search('\((?P<lang>\w+)\)', lines[0])
    return m.group('lang')


def class_files(name, bocca=None, pattern=None):
    """Get user-editable files for a bocca class.

    Parameters
    ----------
    name : str
        Name of class.
    bocca : str, optional
        Path to the bocca program.
    pattern : str
        Glob-style pattern.

    Returns
    -------
    list
        Names of user-editable files.
    """
    from fnmatch import fnmatch

    bocca = bocca or which('bocca')

    files = check_output([bocca, 'display', 'class', '-f', name]).split()
    if pattern:
        return [f for f in files if fnmatch(f, pattern)]
    else:
        return files


def replace_class_name(src, dest, include=None, prefix=None, cflags=None,
                       libs=None):
    """Replace the name of a class in impl files.

    .. note:: Deprecated.

    Parameters
    ----------
    src : str
        Name of source class.
    dest : str
        Name of destination class.
    """
    import re

    cflags = cflags or ''
    libs = libs or ''

    subs = ((re.sub('\.', '_', src), re.sub('\.', '_', dest)),
            (src, dest),
            ('BMI_HEAT', prefix),
            ('bmi_heat.h', include),
            ('Heat', dest.split('.')[-1]),
           )

    for path in class_files(dest):
        f = fileinput.input(path, inplace=True)
        for line in f:
            for sub in subs:
                line = re.sub(sub[0], sub[1], line)
            if line.startswith('INCLUDES ='):
                line = ' '.join([line.rstrip(), cflags])
            elif line.startswith('LIBS ='):
                line = ' '.join([line.rstrip(), libs])

            print line.rstrip()
        f.close()


def substitute_in_file(file_like, pattern, repl):
    """
    .. note:: Deprecated.
    """
    if isinstance(file_like, types.StringTypes):
        with open(file_like, 'r') as fp:
            contents = fp.read()
    else:
        contents = file_like.read()

    return re.sub(pattern, repl, contents)

    if inplace:
        with open(path, 'w') as fp:
            fp.write(contents)


def substitute_patterns(subs, string):
    """Substitute patterns in a string.

    Parameters
    ----------
    subs : iterable
        Iterable of tuples of (*pattern*, *repl*).
    string : str
        String to make substitutions.

    Returns
    -------
    str
        Resulting string with substitutions.
    """
    for pattern, repl in subs:
        string = re.sub(pattern, repl, string)
    return string


def substitute_patterns_in_file(subs, file_like):
    """Substitute patterns in a file.

    Parameters
    ----------
    subs : iterable
        Iterable of tuples of (*pattern*, *repl*).
    file_like : file_like
        File-like object to make substitutions.

    Returns
    -------
    str
        Resulting string with substitutions.
    """
    if isinstance(file_like, types.StringTypes):
        with open(file_like, 'r') as fp:
            contents = fp.read()
    else:
        contents = file_like.read()
    return substitute_patterns(subs, contents)


def replace_c_class_names(paths, src, dest, inplace=True):
    """Replace C class names in impl files.

    Parameters
    ----------
    paths : iterable
        Path to impl files.
    src : str
        Name of source class.
    dest : str
        Name of destination class.
    inplace : boolean, optional
        Make substitutions in-place.
    """
    src_with_underscores = re.sub('\.', '_', src)
    dest_with_underscores = re.sub('\.', '_', dest)
    subs = (
        (src_with_underscores, dest_with_underscores),
        (src, dest),
    )

    for path in paths:
        contents = substitute_patterns_in_file(subs, path)
        if not inplace:
            path = re.sub(src_with_underscores, dest_with_underscores,
                          os.path.basename(path))
        with open(path, 'w') as fp:
            fp.write(contents)


def replace_py_class_names(paths, src, dest, inplace=True):
    """Replace Python class names in impl files.

    Parameters
    ----------
    paths : iterable
        Path to impl files.
    src : str
        Name of source class.
    dest : str
        Name of destination class.
    inplace : boolean, optional
        Make substitutions in-place.
    """
    src_with_underscores = re.sub('\.', '_', src)
    dest_with_underscores = re.sub('\.', '_', dest)
    subs = (
        (src_with_underscores, dest_with_underscores),
        (src, dest),
    )

    for path in paths:
        contents = substitute_patterns_in_file(subs, path)
        if not inplace:
            old_class = src_with_underscores.split('_')[-1]
            new_class = dest_with_underscores.split('_')[-1]
            path = re.sub(old_class, new_class,
                          os.path.basename(path))
        with open(path, 'w') as fp:
            fp.write(contents)


def replace_cxx_class_names(paths, src, dest, inplace=True):
    """Replace C++ class names in impl files.

    Parameters
    ----------
    paths : iterable
        Path to impl files.
    src : str
        Name of source class.
    dest : str
        Name of destination class.
    inplace : boolean, optional
        Make substitutions in-place.
    """
    src_with_underscores = re.sub('\.', '_', src)
    dest_with_underscores = re.sub('\.', '_', dest)
    src_with_colons = re.sub('\.', '::', src)
    dest_with_colons = re.sub('\.', '::', dest)
    subs = (
        (src_with_underscores, dest_with_underscores),
        (src_with_colons, dest_with_colons),
        (src, dest),
    )

    for path in paths:
        contents = substitute_patterns_in_file(subs, path)
        if not inplace:
            path = re.sub(src_with_underscores, dest_with_underscores,
                          os.path.basename(path))
        with open(path, 'w') as fp:
            fp.write(contents)


def replace_bmi_names(paths, mapping):
    """Replace BMI variables in impl files.

    Parameters
    ----------
    paths : iterable
        Paths to impl files.
    mapping : dict
        Mapping to use in substitutsions.
    """
    for path in paths:
        if os.path.isfile(path):
            with open(path, 'r') as fp:
                contents = Template(fp.read()).safe_substitute(mapping)
            with open(path, 'w') as fp:
                fp.write(contents)


def copy_class(src, dest, bocca=None):
    """Copy a bocca class.

    Parameters
    ----------
    src : str
        Name of source class.
    dest : str
        Name of destination class.
    bocca : str, optional
        Path to bocca program.
    """
    bocca = bocca or which('bocca')

    system([bocca, 'copy', 'class', src, dest])

    if class_language(dest) == 'c':
        replace_c_class_names(class_files(dest, pattern='*.[ch]'), src, dest)


def dup_c_impl(path, new, destdir='.'):
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.[ch]')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_c_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_py_impl(path, new, destdir='.'):
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.py')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_py_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)

    #impl_files = (glob.glob(os.path.join(path, '*.[ch]')) +
    #              glob.glob(os.path.join(path, 'make.*.user')))

    #impl_files = []
    shutil.copytree(path, os.path.join(destdir, new))

    #with cd(path) as base:
    #    for fname in os.listdir(path):
    #        if not fname.startswith('.'):
    #            if os.path.isdir(fname):
    #                shutil.copytree(fname, os.path.join(destdir, fname))
    #            else:
    #                shutil.copy(fname, destdir)

    #with cd(os.path.join(destdir, new)) as _:
    #    replace_c_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_cxx_impl(path, new, destdir='.'):
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.cxx')) +
                  glob.glob(os.path.join(path, '*.hxx')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_cxx_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_impl_files(path, new, destdir='.', language=None):
    language = language or guess_language_from_files(path)

    if language == 'c':
        return dup_c_impl(path, new, destdir=destdir)
    elif language == 'cxx':
        return dup_cxx_impl(path, new, destdir=destdir)
    elif language == 'python':
        return dup_py_impl(path, new, destdir=destdir)
    else:
        raise ValueError('language not understood: %s' % language)


def guess_language_from_files(path):
    """Guess the language of a bocca class.

    Parameters
    ----------
    path : str
        Path to a bocca class.

    Returns
    -------
    str
        Language of the class.
    """
    from glob import glob

    with cd(path) as _:
        if len(glob('*.[ch]')) > 0:
            return 'c'
        elif len(glob('*.cxx') + glob('*.hxx')) > 0:
            return 'cxx'
        else:
            return None


_GRID_TYPE_FUNCTIONS = {
    'uniform_rectilinear': [
        'get_grid_shape', 'get_grid_spacing', 'get_grid_origin',
    ],
    'rectilinear': [
        'get_grid_shape', 'get_grid_x', 'get_grid_y',
    ],
    'structured': [
        'get_grid_shape', 'get_grid_x', 'get_grid_y',
    ],
    'unstructured': [
        'get_grid_offset', 'get_grid_connectivity',
    ],
}

def get_grid_type_defines(grid_types):
    """
    .. note:: Deprecated.
    """
    if isinstance(grid_types, types.StringTypes):
        grid_types = [grid_types]

    defines = []
    for grid_type in grid_types:
        for func in _GRID_TYPE_FUNCTIONS[grid_type]:
            defines.append('#define BMI_HAS_%s' % func.upper())

    return os.linesep.join(defines)


def get_interfaces(proj):
    """Get interfaces in a project description.

    Parameters
    ----------
    proj : dict
        Project description.

    Returns
    -------
    list
        Interfaces descriptions.
    """
    interfaces = {}
    for interface in proj.get('interfaces', []):
        name = interface.pop('name')
        interfaces[name] = interface

    return interfaces


def render_include_block(includes):
    """Construct an include block.

    Parameters
    ----------
    includes : iterable or str
        Lines of the include block.

    Returns
    -------
    str
        Include block.
    """
    if not isinstance(includes, types.StringTypes):
        return os.linesep.join(includes)
    return includes


def get_bmis(proj):
    """Get BMI descriptions for a project.

    Parameters
    ----------
    proj : dict
        BMI project description.

    Returns
    -------
    list
        The BMI descriptions in the project.
    """
    bmis = {}
    for bmi in proj.get('bmi', []):
        language = bmi.pop('language')
        name = bmi.pop('name')
        impl = bmi.pop('impl', _PATH_TO_IMPL[language])

        if language in ['c', 'cxx']:
            mapping = {
                'bmi_includes': render_include_block(bmi.get('includes', '')),
                'bmi_register': bmi.get('register', None),
                'bmi_libs': bmi.get('libs', ''),
                'bmi_cflags': bmi.get('cflags', ''),
            }
        elif language in ['python', 'py']:
            mapping = {
                'bmi_package': bmi.get('package', None),
                'bmi_class': bmi.get('class', None),
            }
        else:
            mapping = {}

        bmis[name] = {
            'language': language,
            'impl': impl,
            'bmi_mapping': mapping,
        }

    return bmis


def make_project(proj, clobber=False):
    """Make a bocca project with BMI implementations.

    Parameters
    ----------
    proj : dict
        BMI project description.
    clobber : boolean, optional
        Clobber an existing project if it exists.
    """
    if clobber:
        ifexists = 'clobber'
    else:
        ifexists = 'raise'

    interfaces = get_interfaces(proj)
    bmis = get_bmis(proj)

    bocca = Bocca()
    bocca.create_project(proj['name'], language=proj['language'],
                         ifexists=ifexists)

    with cd(proj['name']) as path:
        for name, interface in interfaces.items():
            bocca.create_interface(name, **interface)

        for name, bmi in bmis.items():
            bocca.create_bmi_class(name, **bmi)
