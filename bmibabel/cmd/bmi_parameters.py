#! /usr/bin/env python
"""Find BMI parameters in a BMI metadata folder."""
from __future__ import print_function

import os
import sys
import re
import argparse
import warnings
import shutil

import yaml

from ..parameters import load


def main():
    """Look for BMI parameters in a folder."""
    parser = argparse.ArgumentParser()
    add_arguments(parser)

    args = parser.parse_args()

    print_defaults(args)


def add_arguments(parser):
    parser.add_argument('path', type=str, help='BMI metadata path')


def print_defaults(args):
    defaults = {}
    for param in load(args.path).values():
        defaults[param.name] = param.value

    print(yaml.dump(defaults, default_flow_style=False), file=sys.stdout)


if __name__ == '__main__':
    main()
