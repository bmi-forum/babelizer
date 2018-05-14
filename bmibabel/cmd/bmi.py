from __future__ import print_function

import sys

from . import bmi_babelize as babelize
from . import bmi_find as find
from . import bmi_parameters as parameters
from . import bmi_stage as stage
from . import bmi_files as files
from . import bmi_install as install


def load_subparsers(subparsers):
    import pkg_resources

    class Plugins(object):
        pass


    plugins = Plugins()


    for entry_point in pkg_resources.iter_entry_points(group='bmi.plugins'):
        try:
            plugin = entry_point.load()
        except Exception as err:
            pass
        else:
            plugin(subparsers)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        fromfile_prefix_chars='@',
    )

    subparsers = parser.add_subparsers(
        title='subcommands',
        description='valid commands',
        help='additional help',
    )
    subparsers.required = True

    babelize.create_parser(addto=subparsers)
    find.create_parser(addto=subparsers)
    parameters.create_parser(addto=subparsers)
    stage.create_parser(addto=subparsers)
    files.create_parser(addto=subparsers)
    install.create_parser(addto=subparsers)

    load_subparsers(subparsers)

    args = parser.parse_args()

    rtn = args.func(args)
