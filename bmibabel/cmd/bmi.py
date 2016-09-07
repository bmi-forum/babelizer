from __future__ import print_function

from . import bmi_babelize as babelize
from . import bmi_find as find
from . import bmi_parameters as parameters
from . import bmi_stage as stage
from . import bmi_files as files
from . import bmi_install as install


def main():
    import argparse

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid commands',
                                       help='additional help')

    babelize.create_parser(addto=subparsers)
    find.create_parser(addto=subparsers)
    parameters.create_parser(addto=subparsers)
    stage.create_parser(addto=subparsers)
    files.create_parser(addto=subparsers)
    install.create_parser(addto=subparsers)

    args = parser.parse_args()

    rtn = args.func(args)
