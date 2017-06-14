#! /usr/bin/env python
"""Stage a BMI model for execution."""
from __future__ import print_function

import os
import sys
import re
import argparse
import shutil

import yaml

from ..stage import stage


def main():
    """Stage a BMI model."""
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


def create_parser(addto=None):
    if addto:
        parser = addto.add_parser('stage', help='stage a model')
    else:
        parser = argparse.ArgumentParser(description='stage a model')

    parser.add_argument('path', type=str, help='BMI metadata path')
    parser.add_argument('dest', type=str, help='stage folder')

    parser.set_defaults(func=lambda args: stage(args.path, args.dest))

    return parser


if __name__ == '__main__':
    main()
