# coding: utf-8
from setuptools import setup, find_packages
from os.path import join, dirname

import django_pathman

setup(
    name='django_pathman',
    version=django_pathman.__version__,
    author='Ruslan Gilfanov',
    author_email='rg@informpartner.com',
    packages=find_packages(),
    data_files=[
        ('sql', ['django_pathman/sql/alter_child_index_v1.sql']),
    ],
    install_requires=[
        'django>=1.9.5',
    ],
)
