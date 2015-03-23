#! /usr/bin/env python
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


class Error(Exception):
    pass


class ProjectExistsError(Error):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Bocca(object):
    def __init__(self, bocca=None):
        self._bocca = bocca or which('bocca')
        if self._bocca is None:
            raise RuntimeError('unable to find bocca')

    @property
    def bocca(self):
        return self._bocca

    def create_project(self, name, language=None, ifexists='raise'):
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
        options = []
        if sidl is not None:
            options += ['--import-sidl=%s@%s' % (name, sidl)]

        system([self.bocca, 'create', 'interface', name] + options)


    def create_class(self, name, implements=None, language=None, sidl=None,
                     impl=None):
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
        bmi_mapping = bmi_mapping or {}

        kwds = dict(implements='csdms.core.Bmi', language=language)
        if impl is None:
            self.create_class(name, **kwds)
        else:
            with mktemp(prefix='csdms', suffix='.d') as destdir:
                kwds['impl'] = make_impl_dir(name, language, subs=bmi_mapping)
                self.create_class(name, **kwds)


def make_impl_dir(name, language, subs=None, destdir='.'):
    subs = subs or {}

    src_impls = _PATH_TO_IMPL[language]

    impl_dir = dup_impl_files(src_impls, name, destdir=destdir,
                              language=language)
    replace_bmi_names(glob.glob(os.path.join(impl_dir, '*')), subs)

    return impl_dir


def is_bocca_project(name):
    return os.path.isdir(os.path.join(name, 'BOCCA'))


def class_language(name, bocca=None):
    bocca = bocca or which('bocca')

    import re

    lines = check_output([bocca, 'display', 'class', name]).split(os.linesep)
    m = re.search('\((?P<lang>\w+)\)', lines[0])
    return m.group('lang')


def class_files(name, bocca=None, pattern=None):
    from fnmatch import fnmatch

    bocca = bocca or which('bocca')

    files = check_output([bocca, 'display', 'class', '-f', name]).split()
    if pattern:
        return [f for f in files if fnmatch(f, pattern)]
    else:
        return files


def replace_class_name(src, dest, include=None, prefix=None, cflags=None,
                       libs=None):
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
    for pattern, repl in subs:
        string = re.sub(pattern, repl, string)
    return string


def substitute_patterns_in_file(subs, file_like):
    if isinstance(file_like, types.StringTypes):
        with open(file_like, 'r') as fp:
            contents = fp.read()
    else:
        contents = file_like.read()
    return substitute_patterns(subs, contents)


def replace_c_class_names(paths, src, dest, inplace=True):
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
    for path in paths:
        if os.path.isfile(path):
            with open(path, 'r') as fp:
                contents = Template(fp.read()).safe_substitute(mapping)
            with open(path, 'w') as fp:
                fp.write(contents)


def copy_class(src, dest, bocca=None):
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
    if isinstance(grid_types, types.StringTypes):
        grid_types = [grid_types]

    defines = []
    for grid_type in grid_types:
        for func in _GRID_TYPE_FUNCTIONS[grid_type]:
            defines.append('#define BMI_HAS_%s' % func.upper())

    return os.linesep.join(defines)


def get_interfaces(proj):
    interfaces = {}
    for interface in proj.get('interfaces', []):
        name = interface.pop('name')
        interfaces[name] = interface

    return interfaces


def render_include_block(includes):
    if not isinstance(includes, types.StringTypes):
        return os.linesep.join(includes)
    return includes


def get_bmis(proj):
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
