#! /usr/bin/env python
from collections import namedtuple

import yaml

from .utils import cd, read_first_of


Parameter = namedtuple('Parameter', ('name', 'value', 'units', 'desc', 'type'))


def validate_parameters(params):
    if not isinstance(params, dict):
        return False
    return True


def load_as_dict(dir='.'):
    with cd(dir):
        fname, contents = read_first_of(['parameters.yaml', 'parameters.yml'])
        parameters = yaml.load(contents)

    if not validate_parameters(parameters):
        raise ValueError(
            '{name}: not a valid parameters file'.format(name=fname))

    return parameters


def load(dir='.'):
    """Load model default parameters from a BMI metadata file.

    Parameters
    ----------
    dir : str
        Path to the folder that contains BMI metadata files.

    Returns
    -------
    dict
        A dictionary of parameter names as keys and namedtuple as values that
        contains a description of the parameter.
    """

    params = {}
    for name, param in load_as_dict(dir).items():
        if name.startswith('_'):
            continue

        try:
            value = param['value']['default']
        except TypeError:
            print name, param, path
            raise

        try:
            units = param['value']['units']
        except KeyError:
            units = '-'
            # warnings.warn('missing units for {name}'.format(
            #     name=name))

        type = param['value']['type']
        if type == 'choice':
            choices = [repr(choice) for choice in param['value']['choices']]
            type = '{' + ', '.join(choices) + '}'
        elif type == 'file':
            type = 'str'

        params[name] = Parameter(name=name, value=value, units=units,
                                 desc=param['description'], type=type)

    return params
