#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name='cump',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'simples3', 'PyYAML', 'requests', 'Click'
    ],
    entry_points='''
        [console_scripts]
        cump=cump.main:cli
    ''',
)