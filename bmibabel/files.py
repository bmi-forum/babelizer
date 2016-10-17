#! /usr/bin/env python
import os
import string
import shutil

from scripting.contexts import cd

from .utils import mkdir_p, is_text_file
from .api import load_api


_METADATA_FILES = {
    'api.yaml', 'api.yml',
    'parameters.yaml', 'parameters.yml',
    'info.yaml', 'info.yml',
    'wmt.yaml', 'wmt.yml',
}


class SafeFormatter(string.Formatter):
    def get_field(self, field_name, args, kwargs):
        try:
            val = super(SafeFormatter, self).get_field(field_name, args,
                                                       kwargs)
        except (KeyError, AttributeError):
            val = '{' + field_name + '}', field_name 

        return val 

    def format_field(self, value, spec):
        try:
            return super(SafeFormatter, self).format_field(value, spec)
        except ValueError:
            return value


def sub_parameters(string, **kwds):
    formatter = SafeFormatter()
    return formatter.format(string, **kwds)


def is_metadata_file(fname):
    return os.path.basename(fname) in _METADATA_FILES


def find_bmi_metadata_files(datadir):
    with cd(datadir, create=False):
        found = [fname for fname in _METADATA_FILES if os.path.isfile(fname)]

    return [os.path.join(datadir, fname) for fname in found]


def find_bmi_data_files(datadir):
    """Look for BMI data files.
    
    Parameters
    ----------
    datadir : str
        Path the the BMI component's data directory.

    Returns
    -------
    list of str
        List of the data files relative to their data directory.
    """
    fnames = []
    for root, dirs, files in os.walk(datadir):
        for dir in dirs:
            fnames.append(os.path.normpath(os.path.join(root, dir)) + os.sep)

        for fname in files:
            if not is_metadata_file(fname):
                fnames.append(os.path.normpath(os.path.join(root, fname)))

    return fnames


def fill_template_file(src, dest, **kwds):
    """Substitute values into a template file.

    Parameters
    ----------
    src : str
        Path to a template file.
    dest : str
        Path to output file that will contain the substitutions.
    """
    (srcdir, fname) = os.path.split(src)
    dest = os.path.abspath(dest)

    with cd(srcdir):
        with open(fname, 'r') as fp:
            template = fp.read()

        (base, ext) = os.path.splitext(dest)
        if ext == '.tmpl':
            dest = base

        with open(dest, 'w') as fp:
            try:
                fp.write(sub_parameters(template, **kwds))
            except ValueError as err:
                raise ValueError(src + ':' + str(err))

    return dest


def stage_data_files(datadir, destdir, **kwds):
    """Copy BMI data files into a folder, filling template files on the way.

    Parameters
    ----------
    datadir : str
        Path to the BMI component's data folder.
    destdir : str
        Path to the folder to copy the data into.
    """
    data_files = copy_data_files(datadir, destdir)

    staged = []
    with cd(destdir):
        for data_file in data_files:
            dest = data_file
            if is_text_file(data_file):
                dest = fill_template_file(data_file, dest, **kwds)
                if not os.path.samefile(dest, data_file):
                    os.remove(data_file)
            staged.append(dest)

    return staged


def copy_data_files(datadir, destdir):
    """Copy BMI data files into a folder.

    Parameters
    ----------
    datadir : str
        Path to the BMI component's data folder.
    destdir : str
        Path to the folder to copy the data into.
    """
    datadir = os.path.abspath(datadir)
    destdir = os.path.abspath(destdir)

    with cd(datadir, create=False):
        data_files = find_bmi_data_files('.')

    copied = []
    with cd(destdir) as cwd:
        for data_file in data_files:
            path_to_src = os.path.join(datadir, data_file)

            dir = os.path.dirname(data_file)
            if dir:
                mkdir_p(dir)

            if os.path.isfile(path_to_src):
                shutil.copy2(path_to_src, data_file)
                copied.append(os.path.abspath(data_file))

    return copied


def install_data_files(path, prefix, include_metadata=False):
    installed = []

    bmi = load_api(path)

    datadir = mkdir_p(os.path.join(prefix, 'share', 'csdms', bmi['name']))
    installed += copy_data_files(bmi['path'], datadir)

    if include_metadata:
        for path_to_src in find_bmi_metadata_files(bmi['path']):
            shutil.copy2(path_to_src, datadir)

    return installed
