from __future__ import print_function

from .bmi_babelize import babelize
from .bmi_find import find
from .bmi_babelize import add_arguments as babelize_add_arguments
from .bmi_find import add_arguments as find_add_arguments


def main():
    import argparse

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid commands',
                                       help='additional help')
    parser_find = subparsers.add_parser(
        'find', help='find BMI metadata folders')
    find_add_arguments(parser_find)
    parser_find.set_defaults(func=find)

    parser_babelize = subparsers.add_parser(
        'babelize', help='use babel to build language bindings')
    babelize_add_arguments(parser_babelize)
    parser_babelize.set_defaults(func=babelize)

    args = parser.parse_args()

    rtn = args.func(args)
