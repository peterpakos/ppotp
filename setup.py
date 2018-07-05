# -*- coding: utf-8 -*-

from os.path import join, dirname, abspath
from setuptools import setup

with open(join(abspath(dirname(__file__)), 'VERSION')) as version_file:
    VERSION = version_file.read().strip()

setup(version=VERSION, data_files=[('ppotp', ['VERSION'])])
