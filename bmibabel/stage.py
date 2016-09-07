#! /usr/bin/env python
import os
import shutil
import string

from .utils import mkdir_p, cd, is_text_file
from .parameters import load
from .files import find_bmi_data_files, fill_template_file


def stage(path, dest):
    params = {}
    for param in load(path).values():
        params[param.name] = param.value

    mkdir_p(dest)
    copy_data_files(path, dest, **params)


def copy_data_files(datadir, destdir, **kwds):
    """Copy BMI data files into a folder, filling template files on the way.

    Parameters
    ----------
    datadir : str
        Path to the BMI component's data folder.
    destdir : str
        Path to the folder to copy the data into.
    """
    with cd(datadir):
        data_files = find_bmi_data_files('.')

    with cd(destdir) as cwd:
        for data_file in data_files:
            path_to_src = os.path.join(datadir, data_file)

            dir = os.path.dirname(data_file)
            if dir:
                mkdir_p(dir)

            if os.path.isfile(path_to_src):
                if is_text_file(path_to_src):
                    fill_template_file(path_to_src, data_file, **kwds)
                else:
                    shutil.copy2(path_to_src, data_file)

