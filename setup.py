from setuptools import setup, find_packages

from codecs import open
from os import path


_HERE = path.abspath(path.dirname(__file__))


def read(*names, **kwds):
    return open(
        path.join(_HERE, *names),
        encoding=kwds.get('encoding', 'utf-8')
    ).read()


def find_version(*file_paths):
    import re

    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='bmibabel',
    version=find_version("bmibabel/__init__.py"),
    description='Generate BMI language bindings with babel.',
    long_description=read('README.md'),
    url='https://github.com/csdms/bmi-babel',

    author='Eric Hutton',
    author_email='hutton.eric@gmail.com',

    license='MIT',

    packages=['bmibabel', 'bmibabel.cmd'],

    entry_points={
        'console_scripts': [
            'bmi-babel-make=bmibabel.cmd.make:main',
            'bmi-babel-fetch=bmibabel.cmd.bmi_babel_fetch:main',
            'bmi-babel-find=bmibabel.cmd.bmi_babel_find:main',
            'bmi-babelize=bmibabel.cmd.bmi_babelize:main',
            'bmi=bmibabel.cmd.bmi:main',
        ],
    },

    package_data={'bmibabel': ['data/*sidl', 'data/c.Component/*', 'data/py.Component/*']},
)
