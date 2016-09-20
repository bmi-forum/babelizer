#! /usr/bin/env python
"""Fetch remote BMI models."""
from __future__ import print_function

import sys
import argparse

from ..build import babelize


def main():
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


def create_parser(addto=None):
    if addto:
        parser = addto.add_parser(
            'babelize', help='use babel to build language bindings',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    else:
        parser = argparse.ArgumentParser(
            description='use babel to build language bindings',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('path', type=str, nargs='+',
                        help='Path to BMI metadta.')
    parser.add_argument('--prefix', type=str, default=sys.prefix,
                        help='Prefix for installation')
    parser.add_argument(
        '--no-build', dest='build', action='store_false',
        help='stage project but do not build')
    parser.add_argument(
        '--no-install', dest='install', action='store_false',
        help='stage and build project but do not install')

    parser.set_defaults(func=lambda args: babelize(args.path, prefix=args.prefix, build=args.build, install=args.install))

    return parser


if __name__ == '__main__':
    main()
