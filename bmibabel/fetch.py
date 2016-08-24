#! /usr/bin/env python
"""Fetch remote BMI models."""
from __future__ import print_function

import os
import sys
import re
import warnings

import yaml

from .utils import cd
from .git import git_repo_name, git_clone_or_update, git_repo_sha
from .project import empty_bmi_project, add_bmi_component
from . import api
from .errors import MissingFileError, ParseError


def _cache_dir_from_repo(repo, branch='master'):
    """Name of cache directory for a git repository.

    Parameters
    ----------
    repo : str
        URL of git repository.
    branch : str, optional
        Branch of the git repository.

    Returns
    -------
    str
        Name of the directory to use for the cache.
    """
    cache_dir = '{repo}-{sha}'.format(repo=git_repo_name(repo),
                                      sha=git_repo_sha(repo, branch=branch))
    return os.path.join('cache', cache_dir)


def _component_name_from_repo(repo, name=None):
    """Get fully-qualified component name from repository name.

    Parameters
    ----------
    repo : str
        Name of a repository.
    name : str, optional
        Name of component.

    Returns
    -------
    str
        Fully-qualified component name.
    """
    name = name or re.sub('-', '', os.path.basename(repo).title())

    return '.'.join(['model', name])


def _parse_repo_line(line):
    """Parse a line containing the location of a BMI repository.

    Parameters
    ----------
    line : str
        Location of repository.

    Returns
    -------
    (repo, branch)
        Tuple of repository url, and a branch name.
    """
    if ',' in line:
        repo, branch = line.split(',')
    else:
        repo, branch = line, 'master'

    return repo.strip(), branch.strip()


def _get_bmi_from_repo(repo, prefix='/usr/local', build_api=False):
    """Get BMI description from a git repository.

    Parameters
    ----------
    repo : str
        url or path to repository.
    prefix : str
        Path to installation prefix for BMI implementation

    Returns
    -------
    dict
        BMI description.
    """
    if repo.startswith('http'):
        repo, branch = _parse_repo_line(repo)

        cache_dir = _cache_dir_from_repo(repo, branch=branch)

        git_clone_or_update(repo, dir=cache_dir, branch=branch)
    else:
        cache_dir = repo

    with cd(cache_dir) as _:
        if build_api:
            api.execute_api_build(prefix=prefix)
        bmi = api.load_all()

    #bmi['name'] = _component_name_from_repo(repo, bmi.get('name', None))

    return bmi


def fetch_bmi_components(repos, install_prefix='/usr/local', build_api=False):
    proj = load_bmi_components(repos, install_prefix=install_prefix,
                               build_api=False)

    return yaml.dump(proj, default_flow_style=False)


def load_bmi_components(repos, install_prefix='/usr/local', build_api=False):
    proj = empty_bmi_project()
    for repo in repos:
        try:
            add_bmi_component(proj,
                              _get_bmi_from_repo(repo, prefix=install_prefix,
                                                 build_api=build_api))
        except MissingFileError as err:
            warnings.warn('Skipping %s: missing file (%s)' % (repo, err))
        except ParseError as err:
            warnings.warn('Skipping %s: parse error (%s)' % (repo, err))

    return proj
