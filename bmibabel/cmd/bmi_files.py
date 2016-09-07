#! /usr/bin/env python
"""Stage a BMI model for execution."""
from __future__ import print_function

import os
import sys
import re
import argparse
import warnings
import shutil

import yaml

from ..files import find_bmi_data_files


def main():
    """Find data files."""
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


def print_data_files(args):
    print(yaml.dump(find_bmi_data_files(args.path), default_flow_style=False),
          file=sys.stdout)


def create_parser(addto=None):
    if addto:
        parser = addto.add_parser('files', help='BMI data files')
    else:
        parser = argparse.ArgumentParser(description='BMI data files')

    parser.add_argument('path', type=str, help='BMI metadata path')

    parser.set_defaults(func=print_data_files)

    return parser


if __name__ == '__main__':
    main()
