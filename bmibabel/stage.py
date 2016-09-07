#! /usr/bin/env python
import os
import shutil
import string

from .utils import mkdir_p
from .parameters import load
from .files import copy_data_files


def stage(path, dest):
    params = {}
    for param in load(path).values():
        params[param.name] = param.value

    mkdir_p(dest)
    copy_data_files(path, dest, **params)
