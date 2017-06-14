#! /usr/bin/env python
"""Fetch remote BMI models."""
from __future__ import print_function

import os
import sys
import re
import argparse
import shutil

import yaml

from ..fetch import fetch_bmi_components

from ..utils import cd
from ..git import git_repo_name, git_clone_or_update, git_repo_sha
from ..project import empty_bmi_project, add_bmi_component
from .. import api
from ..errors import MissingFileError, ParseError


def scan_repos_from_file(fname):
    """Read repositories from a file.

    Parameters
    ----------
    fname : str
        Name of file containing repositories.

    Returns
    -------
    list
        List of repositories.
    """
    with open(fname, 'r') as file_like:
        repos = yaml.load(file_like)

    return repos


def main():
    """Get a remote BMI implementation and build it."""
    parser = argparse.ArgumentParser()

    parser.add_argument('repo', type=str, nargs='*',
                        help='GitHub repository for BMI implementation')
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

    repos = args.repo
    if args.file:
        repos += scan_repos_from_file(args.file)

    description = fetch_bmi_components(repos, install_prefix=args.prefix,
                                       build_api=args.build_api)

    print(description, file=sys.stdout)

    if args.output is not None:
        for item in yaml.load(description)['bmi']:
            dest_dir = os.path.join(args.output, item['name'])
            shutil.copytree(item['path'], dest_dir)


if __name__ == '__main__':
    main()
