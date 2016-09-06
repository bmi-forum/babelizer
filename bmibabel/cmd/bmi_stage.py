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

from ..stage import stage


def main():
    """Stage a BMI model."""
    parser = argparse.ArgumentParser()
    add_arguments(parser)

    args = parser.parse_args()

    stage_model(args)


def add_arguments(parser):
    parser.add_argument('path', type=str, help='BMI metadata path')
    parser.add_argument('dest', type=str, help='stage folder')


def stage_model(args):
    stage(args.path, args.dest)


class StageSubCommand(object):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='BMI metadata path')

    def run(self, args):
        stage_model(args.path, args.dest)


if __name__ == '__main__':
    main()
