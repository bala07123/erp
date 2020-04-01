# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in iffl/__init__.py
from iffl import __version__ as version

setup(
	name='iffl',
	version=version,
	description='iff',
	author='lserp',
	author_email='balamurugan.a@lyncspace.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
