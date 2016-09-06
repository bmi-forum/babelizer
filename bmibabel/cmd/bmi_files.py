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
    parser = argparse.ArgumentParser()
    add_arguments(parser)

    args = parser.parse_args()

    find_files(args)


def add_arguments(parser):
    parser.add_argument('path', type=str, help='BMI metadata path')


def print_data_files(args):
    print(yaml.dump(find_bmi_data_files(args.path), default_flow_style=False),
          file=sys.stdout)


if __name__ == '__main__':
    main()
