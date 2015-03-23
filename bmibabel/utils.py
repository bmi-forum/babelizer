#! /usr/bin/env python
"""General utilities."""

from __future__ import print_function

import os
import sys
import subprocess
import types
import tempfile
import shutil

import yaml
from distutils.dir_util import mkpath


class cd(object):

    """Context for changing the working directory."""

    def __init__(self, dir):
        """Create a new working directory context.

        If *dir* does not exist, it (along with it's parents) will be
        created.

        Parameters
        ----------
        dir : str
            Path to the working directory.
        """
        self._dir = dir

    def __enter__(self):
        self._starting_dir = os.path.abspath(os.getcwd())
        if not os.path.isdir(self._dir):
            mkpath(self._dir)
        os.chdir(self._dir)
        return os.path.abspath(os.getcwd())

    def __exit__(self, type, value, traceback):
        os.chdir(self._starting_dir)


class cdtemp(object):

    """Context that creates a temporary working directory."""

    def __init__(self, **kwds):
        """Create a temporary directory context.

        The keywords are the same as those for ``tempfile.mkdtemp``. After
        exiting the context, the temporary directory is removed.

        See Also
        --------
        mktemp
        """
        self._kwds = kwds
        self._tmp_dir = None

    def __enter__(self):
        self._starting_dir = os.path.abspath(os.getcwd())
        self._tmp_dir = tempfile.mkdtemp(**self._kwds)
        os.chdir(self._tmp_dir)
        return os.path.abspath(self._tmp_dir)

    def __exit__(self, type, value, traceback):
        os.chdir(self._starting_dir)
        shutil.rmtree(self._tmp_dir)


class mktemp(object):

    """Context that creates a temporary directory."""

    def __init__(self, **kwds):
        """Create a temporary directory context.

        The keywords are the same as those for ``tempfile.mkdtemp``. After
        exiting the context, the temporary directory is removed. This is the
        same as :func:`cdtemp` except that the working directory is not
        changed while in the context.

        See Also
        --------
        cdtemp
        """
        self._kwds = kwds
        self._tmp_dir = None

    def __enter__(self):
        self._tmp_dir = tempfile.mkdtemp(**self._kwds)
        return os.path.abspath(self._tmp_dir)

    def __exit__(self, type, value, traceback):
        shutil.rmtree(self._tmp_dir)


def status(message):
    """Print a status message.

    Parameters
    ----------
    message : str
        Status message.
    """
    print(' '.join(['==>', message]), file=sys.stderr)


def check_output(*args, **kwds):
    """Execute a shell command.

    This is the same as the ``subprocess.check_output`` command available in
    Python versions greater than 2.7 but is provided for pre-2.7 versions.
    """
    kwds.setdefault('stdout', subprocess.PIPE)
    return subprocess.Popen(*args, **kwds).communicate()[0]


def system(*args, **kwds):
    """Execute and echo a shell command.

    Parameters
    ----------
    verbose : boolean
        Print ouput.
    """
    verbose = kwds.pop('verbose', True)
    kwds.setdefault('stdout', sys.stderr)

    status(' '.join(args[0]))

    if verbose:
        call = subprocess.check_call
    else:
        call = check_output

    try:
        call(*args, **kwds)
    except subprocess.CalledProcessError:
        status('Error')
        raise


def which(prog, env=None):
    """Look for a program.

    Use the system ``which`` command to look for a program. If provided,
    *env* is the name of a environment variable that may give the path to
    the program.

    Parameters
    ----------
    prog : str
        Name of a program.
    env : str
        Look for program in a user environment.

    Returns
    -------
    str
        The absolute path to the program.
    """
    prog = os.environ.get(env or prog.upper(), prog)

    try:
        prog = check_output(['which', prog],
                            stderr=open('/dev/null', 'w')).strip()
    except subprocess.CalledProcessError:
        return None
    else:
        return prog


def pkg_config(name, opts):
    """Execute the pkg-config command.

    Parameters
    ----------
    name : str
        Name of a pkg-config package.
    opts : str or iterable
        Command-line options to pass to pkg-config.

    Returns
    -------
    str
        Result of calling ``pkg-config``.
    """
    if isinstance(opts, types.StringTypes):
        opts = [opts]

    try:
        flags = check_output([which('pkg-config')] + opts + [name],
                             stderr=open('/dev/null', 'w')).strip()
    except subprocess.CalledProcessError:
        return None
    else:
        return flags


def read_first_of(files):
    """Read the first file found.

    Parameters
    ----------
    files : iterable
        Ordered list of files to read.

    Returns
    -------
    str
        Contents of the first file found, or an empty string.
    """
    for name in files:
        with open(name, 'r') as fp:
            return fp.read()
    return ''
