#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

from opps import social


install_requires = ["opps"]

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Django",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.rst').read()
except:
    long_description = social.__description__

setup(
    name='opps-social',
    namespace_packages=['opps', 'opps.social'],
    version=social.__version__,
    description=social.__description__,
    long_description=long_description,
    classifiers=classifiers,
    keywords='social opps cms django apps magazines websites',
    author=social.__author__,
    author_email=social.__email__,
    url='http://oppsproject.org',
    download_url="https://github.com/opps/opps-social/tarball/master",
    license=social.__license__,
    packages=find_packages(exclude=('doc', 'docs',)),
    package_dir={'opps': 'opps'},
    install_requires=install_requires,
)