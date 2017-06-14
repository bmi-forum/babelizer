#! /usr/bin/env python
"""Stage a BMI model for execution."""
from __future__ import print_function

import os
import sys
import re
import argparse
import shutil

import yaml

from ..files import install_data_files


def main():
    """Find data files."""
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


def create_parser(addto=None):
    if addto:
        parser = addto.add_parser('install', help='install BMI data files')
    else:
        parser = argparse.ArgumentParser(description='install BMI data files')

    parser.add_argument('path', type=str, help='BMI metadata path')
    parser.add_argument('dest', type=str, help='installation prefix')

    parser.set_defaults(func=lambda args: install_data_files(args.path,
                                                             args.dest))

    return parser


if __name__ == '__main__':
    main()
