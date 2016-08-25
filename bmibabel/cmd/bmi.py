from __future__ import print_function

from .bmi_babel_build import babelize, add_arguments


def find(args):
    print('finding...')


def main():
    import argparse

    parser = argparse.ArgumentParser()

    # parser.add_argument('PATH', nargs='+',
    #                     help='paths to BMI metadata')

    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid commands',
                                       help='additional help')
    parser_find = subparsers.add_parser(
        'find', help='find BMI metadata folders')
    parser_find.set_defaults(func=find)

    parser_babelize = subparsers.add_parser(
        'babelize', help='use babel to build language bindings')
    add_arguments(parser_babelize)
    parser_babelize.set_defaults(func=babelize)

    args = parser.parse_args()
    print(args)
    rtn = args.func(args)
