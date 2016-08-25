#! /usr/bin/env python
"""Fetch remote BMI models."""
from __future__ import print_function

import os
import sys
import re
import argparse
import warnings
import shutil

import yaml

from ..fetch import load_bmi_components

from ..utils import cd, system, mkdir_p, glob_cp
from ..git import git_repo_name, git_clone_or_update, git_repo_sha
from ..project import empty_bmi_project, add_bmi_component
from .. import api
from ..errors import MissingFileError, ParseError
from ..bocca import make_project, build_project, ProjectExistsError


def main():
    parser = argparse.ArgumentParser()
    add_arguments(parser)

    args = parser.parse_args()

    babelize(args)


def add_arguments(parser):
    parser.add_argument('path', type=str, nargs='+',
                        help='Path to BMI metadta.')
    parser.add_argument('--prefix', type=str, default='/usr/local/csdms',
                        help='Prefix for installation')
    parser.add_argument(
        '--no-build', dest='build', action='store_false',
        help='stage project but do not build')
    parser.add_argument(
        '--no-install', dest='install', action='store_false',
        help='stage and build project but do not install')


def babelize(args):
    proj = load_bmi_components(args.path, install_prefix=args.prefix,
                               build_api=False)

    try:
        build_dir = make_project(proj, clobber=True)
    except ProjectExistsError as error:
        print('The specified project (%s) already exists. Exiting.' % error)
        return None

    if args.build:
        build_project(build_dir, prefix=args.prefix, install=args.install)

        if args.install:
            proj = load_bmi_components(args.path, install_prefix=args.prefix,
                                       build_api=False)
            for bmi in proj['bmi']:
                try:
                    datadir = mkdir_p(os.path.join(args.prefix, 'share',
                                                   'csdms', bmi['name']))
                except KeyError:
                    print(bmi)
                else:
                    glob_cp(os.path.join(bmi['path'], '*'), datadir)


if __name__ == '__main__':
    main()
