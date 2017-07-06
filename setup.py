# coding: utf-8
from setuptools import setup, find_packages
from os.path import join, dirname

import django_pathman

setup(
    name='django_pathman',
    version=django_pathman.__version__,
    packages=find_packages(),
    # long_description=open(join(dirname(__file__), 'README.txt')).read(),
    package_data={'sql': ['sql/*.sql', 'sql/README']},
    install_requires=[
        'django>=1.9.5',
    ],
)
