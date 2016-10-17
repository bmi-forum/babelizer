#! /usr/bin/env python
"""Some bocca utilities."""

import os
import sys
import types
import re
import shutil
import glob
from string import Template

from conda_build.os_utils.macho import get_dylibs

from scripting.unix import system, which, glob_cp, check_output
from scripting.contexts import cd

from .utils import mktemp, mkdir_p, glob_sub
from .errors import ProjectExistsError


_THIS_DIR = os.path.dirname(__file__)
_PATH_TO_IMPL = {
    'c': os.path.join(_THIS_DIR, 'data', 'c.Component'),
    'cxx': os.path.join(_THIS_DIR, 'data', 'csdms.examples.cxx.Heat'),
    'f90': os.path.join(_THIS_DIR, 'data', 'csdms.examples.f90.Heat'),
    'python': os.path.join(_THIS_DIR, 'data', 'py.Component'),
}

_PATH_TO_SIDL = os.path.join(_THIS_DIR, 'data')


def normalize_class_name(name):
    return ''.join([s[0].upper() + s[1:] for s in name.split('_')])


class Bocca(object):

    """Build babel projects with bocca."""

    def __init__(self, bocca=None):
        """Create an instance of a bocca command.

        Parameters
        ----------
        bocca : str
            Path to *bocca* command.
        """
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
                         impl=None):
        """Create a class that implements the Basic Model Interface.

        Parameters
        ----------
        name : str
            Name of the new interface.
        bmi_mapping : dict_like
            Substitutions to make in the implementation files.
        language : {'c', 'cxx', 'python'}
            Language of the class implementation.
        impl : str, optional
            Path to folder containing implementation files to import.
        """
        bmi_mapping = bmi_mapping or {}

        if not name.startswith('csdms.'):
            name = 'csdms.' + name

        class_name = name.split('.')[-1]
        name = '.'.join(name.split('.')[:-1] +
                        [normalize_class_name(class_name)])

        kwds = dict(implements='csdms.core.Bmi', language=language)
        if impl is None:
            self.create_class(name, **kwds)
        else:
            with mktemp(prefix='csdms', suffix='.d') as _:
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
        Absolute path to new impl folder.
    """
    subs = subs or {}
    subs.setdefault('name', name.split('.')[-1])

    src_impls = _PATH_TO_IMPL[language]

    impl_dir = dup_impl_files(src_impls, name, destdir=destdir,
                              language=language)
    replace_bmi_names(glob.glob(os.path.join(impl_dir, '*')), subs)

    return os.path.abspath(impl_dir)


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

    lines = check_output([bocca, 'display', 'class', name]).split(os.linesep)
    return re.search(r'\((?P<lang>\w+)\)', lines[0]).group('lang')


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
        with open(file_like, 'r') as file_like:
            contents = file_like.read()
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
    src_with_underscores = re.sub(r'\.', '_', src)
    dest_with_underscores = re.sub(r'\.', '_', dest)
    subs = (
        (src_with_underscores, dest_with_underscores),
        (src, dest),
    )

    for path in paths:
        contents = substitute_patterns_in_file(subs, path)
        if not inplace:
            path = re.sub(src_with_underscores, dest_with_underscores,
                          os.path.basename(path))
        with open(path, 'w') as file_like:
            file_like.write(contents)


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
    src_with_underscores = re.sub(r'\.', '_', src)
    dest_with_underscores = re.sub(r'\.', '_', dest)
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
            (base, ext) = os.path.splitext(path)
            if ext == '.tmpl':
                path = base
        with open(path, 'w') as file_like:
            file_like.write(contents)


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
    src_with_underscores = re.sub(r'\.', '_', src)
    dest_with_underscores = re.sub(r'\.', '_', dest)
    src_with_colons = re.sub(r'\.', '::', src)
    dest_with_colons = re.sub(r'\.', '::', dest)
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
        with open(path, 'w') as file_like:
            file_like.write(contents)


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
            with open(path, 'r') as file_like:
                contents = Template(file_like.read()).safe_substitute(mapping)
            with open(path, 'w') as file_like:
                file_like.write(contents)


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
    """Duplicate C implementation files.

    Parameters
    ----------
    path : str
        Path to directory containing source impl files.
    new : str
        Name of new class.
    destdir : str, optional
        Path to directory to put duplicated impl files.

    Returns
    -------
    str
        Path to new implementation files.
    """
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.[ch]')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_c_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_py_impl(path, new, destdir='.'):
    """Duplicate Python implementation files.

    Parameters
    ----------
    path : str
        Path to directory containing source impl files.
    new : str
        Name of new class.
    destdir : str, optional
        Path to directory to put duplicated impl files.

    Returns
    -------
    str
        Path to new implementation files.
    """
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.py.tmpl')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_py_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_cxx_impl(path, new, destdir='.'):
    """Duplicate C++ implementation files.

    Parameters
    ----------
    path : str
        Path to directory containing source impl files.
    new : str
        Name of new class.
    destdir : str, optional
        Path to directory to put duplicated impl files.

    Returns
    -------
    str
        Path to new implementation files.
    """
    old = os.path.basename(path)

    impl_files = (glob.glob(os.path.join(path, '*.cxx')) +
                  glob.glob(os.path.join(path, '*.hxx')) +
                  glob.glob(os.path.join(path, 'make.*.user')))

    with cd(os.path.join(destdir, new)) as _:
        replace_cxx_class_names(impl_files, old, new, inplace=False)

    return os.path.join(destdir, new)


def dup_impl_files(path, new, destdir='.', language=None):
    """Duplicate implementation files.

    Parameters
    ----------
    path : str
        Path to directory containing source impl files.
    new : str
        Name of new class.
    destdir : str, optional
        Path to directory to put duplicated impl files.
    language : {'c', 'cxx', 'python'}, optional
        Language of the implementation.

    Returns
    -------
    str
        Path to new implementation files.
    """
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
    with cd(path) as _:
        if len(glob.glob('*.[ch]')) > 0:
            return 'c'
        elif len(glob.glob('*.cxx') + glob.glob('*.hxx')) > 0:
            return 'cxx'
        else:
            return None


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

    with cd(proj['name']) as _:
        for name, interface in interfaces.items():
            bocca.create_interface(name, **interface)

        for name, bmi in bmis.items():
            bocca.create_bmi_class(name, **bmi)

    return os.path.abspath(proj['name'])


def install_name_change(path, old, new):
    system(['install_name_tool', '-change', old, new, path])


def fix_dylibs(path, prefix_to_fix):
    prefix_rpath_to_relpaths(path)
    make_abspath_relative_to_rpath(path, prefix_to_fix)


def make_abspath_relative_to_rpath(path, prefix):
    if prefix.endswith('/'):
        prefix = prefix[:-1]

    for dylib in get_dylibs(path):
        if dylib.startswith(prefix):
            install_name_change(path, dylib, re.sub(prefix, '@rpath', dylib))


def prefix_rpath_to_relpaths(path):
    for dylib in get_dylibs(path):
        if not os.path.isabs(dylib) and not dylib.startswith('@'):
            install_name_change(path, dylib, os.path.join('@rpath', dylib))


def build_project(dir='.', prefix=None, install=False):
    prefix = os.path.abspath(prefix or os.path.join(dir, 'install'))

    libdir = os.path.join(prefix, 'lib')
    sharedir = os.path.join(prefix, 'share')
    site_packages = os.path.join(libdir, 'python2.7', 'site-packages')

    if sys.platform == 'darwin':
        os.environ['LDFLAGS'] = '-headerpad_max_install_names'

    with cd(dir) as cwd:
        system(['./configure', '--with-languages=python c',
                '--prefix={prefix}'.format(prefix=prefix)])
        system(['make', 'all'])

    if install:
        with cd (dir) as cwd:
            system(['make', 'install'])

            libdir = mkdir_p(libdir)
            sharedir = mkdir_p(os.path.join(sharedir, 'cca'))
            site_packages = mkdir_p(os.path.join(site_packages, 'csdms'))

            sub = (os.path.join(cwd, 'install'),
                   os.path.abspath(prefix))
            glob_sub('./install/share/cca/*.cca', sub)
            glob_sub('./install/lib/libcsdms*la', sub)
            for lib in glob.glob('./install/lib/libcsdms*dylib'):
                fix_dylibs(lib, os.path.join(cwd, 'install'))

            glob_cp('./install/share/cca/*.cca', sharedir)
            glob_cp('./install/lib/libcsdms*', libdir)
            glob_cp('./install/lib/python2.7/site-packages/csdms/*py',
                    site_packages)
