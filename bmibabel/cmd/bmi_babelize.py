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

from scripting.contexts import homebrew_hidden, cd, system, mkdir_p, glob_cp

from ..fetch import load_bmi_components

# from ..utils import cd, system, mkdir_p, glob_cp

from ..bocca import make_project, build_project, ProjectExistsError
from ..files import install_data_files


def main():
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


def babelize(args):
    with homebrew_hidden():
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
                    install_data_files(bmi['path'], args.prefix,
                                       include_metadata=True)


def create_parser(addto=None):
    if addto:
        parser = addto.add_parser(
            'babelize', help='use babel to build language bindings')
    else:
        parser = argparse.ArgumentParser(
            description='use babel to build language bindings')

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

    parser.set_defaults(func=babelize)

    return parser


if __name__ == '__main__':
    main()
