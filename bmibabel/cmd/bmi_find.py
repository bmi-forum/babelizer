#! /usr/bin/env python
"""Find BMI descriptions in a directory tree."""
from __future__ import print_function

import os
import sys
import re
import argparse
import shutil

import yaml

from ..api import find_bmi_metadata

from ..utils import cd
from ..git import git_repo_name, git_clone_or_update, git_repo_sha
from ..project import empty_bmi_project, add_bmi_component
from .. import api
from ..errors import MissingFileError, ParseError


def main():
    """Look for BMI metadata in a folder."""
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


def find(args):
    found = set()
    for path in args.path:
        found |= set(find_bmi_metadata(path))

    print(os.linesep.join(found), file=sys.stdout)


def create_parser(addto=None):
    if addto:
        parser = addto.add_parser('find', help='find BMI metadata folders')
    else:
        parser = argparse.ArgumentParser(
            description='find BMI metadata folders')

    parser.add_argument('path', type=str, nargs='+', help='Search paths')
    parser.set_defaults(func=find)

    return parser


if __name__ == '__main__':
    main()
