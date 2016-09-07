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
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


def print_defaults(args):
    defaults = {}
    for param in load(args.path).values():
        defaults[param.name] = param.value

    print(yaml.dump(defaults, default_flow_style=False), file=sys.stdout)


def create_parser(addto=None):
    if addto:
        parser = addto.add_parser('parameters', help='get model parameters')
    else:
        parser = argparse.ArgumentParser(description='get model parameters')
    parser.add_argument('path', type=str, help='BMI metadata path')
    parser.set_defaults(func=print_defaults)

    return parser


if __name__ == '__main__':
    main()
