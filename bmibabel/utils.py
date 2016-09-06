#! /usr/bin/env python
"""General utilities."""

from __future__ import print_function

import os
import sys
import subprocess
import types
import tempfile
import shutil
import glob
import re
import string

from distutils.dir_util import mkpath

from .errors import MissingFileError


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
        self._starting_dir = None

    def __enter__(self):
        """Change to new working directory.

        Returns
        -------
        str
            Absolute path of new working directory.
        """
        self._starting_dir = os.path.abspath(os.getcwd())
        if not os.path.isdir(self._dir):
            mkpath(self._dir)
        os.chdir(self._dir)
        return os.path.abspath(os.getcwd())

    def __exit__(self, ex_type, ex_value, traceback):
        """Change to original working directory."""
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
        self._starting_dir = None
        self._tmp_dir = None

    def __enter__(self):
        """Change to new temporary directory.

        Returns
        -------
        str
            Absolute path of temporary directory.
        """
        self._starting_dir = os.path.abspath(os.getcwd())
        self._tmp_dir = tempfile.mkdtemp(**self._kwds)
        os.chdir(self._tmp_dir)
        return os.path.abspath(self._tmp_dir)

    def __exit__(self, ex_type, ex_value, traceback):
        """Change to original working directory and clean up."""
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
        """Make temporary directory.

        Returns
        -------
        str
            Absolute path of temporary directory.
        """
        self._tmp_dir = tempfile.mkdtemp(**self._kwds)
        return os.path.abspath(self._tmp_dir)

    def __exit__(self, ex_type, ex_value, traceback):
        """Remove temporary directory."""
        shutil.rmtree(self._tmp_dir)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as err:
        if err.errno == os.errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

    return os.path.abspath(path)


def glob_cp(pattern, dest):
    if not os.path.isdir(dest):
        raise ValueError('{dest}: not a directory'.format(dest=dest))

    for fname in glob.glob(pattern):
        status('cp {src} {dest}'.format(src=fname, dest=dest))
        shutil.copy2(fname, dest)


def sub(fname, subs, inplace=False):
    old, new = subs

    with open(fname, 'r') as fp:
        contents = fp.read()
    contents = re.sub(old, new, contents)

    if inplace:
        shutil.copy2(fname, fname + '.bak')
        with open(fname, 'w') as fp:
            fp.write(contents)
    else:
        return contents


def glob_sub(pattern, subs):
    old, new = subs
    for fname in glob.glob(pattern):
        sub(fname, (old, new), inplace=True)


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
    (str, str)
        Name of the first file found and then contents of that file.
    """
    for name in files:
        try:
            with open(name, 'r') as file_like:
                return (os.path.abspath(name), file_like.read())
        except IOError:
            pass
    raise MissingFileError(', '.join(files))


TEXT_CHARACTERS = ''.join(map(chr, range(32, 127)) + list("\n\r\t\b"))
NULL_TRANS = string.maketrans("", "")


def is_text_file(fname, block=1024):
    """Check if a file is text or binary."""
    with open(fname, 'r') as fp:
        return is_text(fp.read(block))


def is_text(buff):
    """Check if a string is text or binary."""
    if '\0' in buff:
        return False

    if len(buff) == 0:
        return True

    bin_chars = buff.translate(NULL_TRANS, TEXT_CHARACTERS)

    if len(bin_chars) > len(buff) * 0.3:
        return False

    return True
