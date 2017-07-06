# coding: utf-8
from setuptools import setup, find_packages
from os.path import join, dirname

import django_pathman

setup(
    name='mq_consumer',
    version=django_pathman.__version__,
    packages=find_packages(),
    # long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=[
        'pika==0.10.0',
    ],
)
