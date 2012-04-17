# coding: utf-8

import glob, sys
from distutils.core import setup
try:
    from setuptools import setup
except ImportError:
    pass


version = '0.2.1'

setup(
    name="taxon",
    version=version,
    description=("Provides simple object taxonomy."),
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: Public Domain",
                 "Programming Language :: Python",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    author="Yasushi Masuda",
    author_email="whosaysni at gmail.com",
    url="http://github.com/whosaysni/taxon/",
    license="Public Domain",
    zip_safe=True,
    packages=["taxon"],
    test_suite = 'tests.suite',
    )
