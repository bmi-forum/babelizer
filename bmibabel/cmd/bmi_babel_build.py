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

    parser.add_argument('path', type=str, nargs='+',
                        help='Path to BMI metadta.')
    parser.add_argument('--prefix', type=str, default='/usr/local/csdms',
                        help='Prefix for installation')
    parser.add_argument('--no-build', dest='build_api', action='store_false',
                        default=True,
                        help='Get API info but do not build')
    parser.add_argument('--file', type=str, default=None,
                        help='Repos file')
    parser.add_argument('--output', type=str, default=None,
                        help='Copy metadata files to a folder')

    args = parser.parse_args()

    # repos = args.repo
    # if args.file:
    #     repos += scan_repos_from_file(args.file)

    proj = load_bmi_components(args.path, install_prefix=args.prefix,
                               build_api=False)

    # print(description, file=sys.stdout)

    try:
        build_dir = make_project(proj, clobber=True)
    except ProjectExistsError as error:
        print('The specified project (%s) already exists. Exiting.' % error)
    else:
        build_project(build_dir, prefix=args.prefix, install=True)

    proj = load_bmi_components(args.path, install_prefix=args.prefix,
                               build_api=False)
    for bmi in proj['bmi']:
        try:
            datadir = mkdir_p(os.path.join(args.prefix, 'share', 'csdms',
                                           bmi['name']))
        except KeyError:
            print(bmi)
        else:
            glob_cp(os.path.join(bmi['path'], '*'), datadir)

    # if args.output is not None:
    #     for item in yaml.load(description)['bmi']:
    #         dest_dir = os.path.join(args.output, item['name'])
    #         shutil.copytree(item['path'], dest_dir)


if __name__ == '__main__':
    main()
