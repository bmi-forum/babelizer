#! /usr/bin/env python
import os
import string

from .utils import cd


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
            fp.write(sub_parameters(template, **kwds))
