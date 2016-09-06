from __future__ import print_function

from .bmi_babelize import babelize
from .bmi_find import find
from .bmi_parameters import print_defaults
from .bmi_stage import stage_model
from .bmi_files import print_data_files

from .bmi_babelize import add_arguments as babelize_add_arguments
from .bmi_find import add_arguments as find_add_arguments
from .bmi_parameters import add_arguments as parameters_add_arguments
from .bmi_stage import add_arguments as stage_add_arguments
from .bmi_files import add_arguments as files_add_arguments


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

    parser_parameters = subparsers.add_parser(
        'parameters', help='get model parameters')
    parameters_add_arguments(parser_parameters)
    parser_parameters.set_defaults(func=print_defaults)

    parser_stage = subparsers.add_parser(
        'stage', help='stage a model')
    stage_add_arguments(parser_stage)
    parser_stage.set_defaults(func=stage_model)

    parser_files = subparsers.add_parser(
        'files', help='BMI data files')
    files_add_arguments(parser_files)
    parser_files.set_defaults(func=print_data_files)

    args = parser.parse_args()

    rtn = args.func(args)
