# coding: utf-8

import glob, sys
from distutils.core import setup
try:
    from setuptools import setup
except ImportError:
    pass


version = '0.1.0'

setup(
    name="taxon",
    version=version,
    description=("Provides simple object taxonomy."),
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: BSD License",
                 "Programming Language :: Python",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    author="Yasushi Masuda",
    author_email="whosaysni at gmail.com",
    url="",
    license="BSD",
    zip_safe=True,
    packages=["taxon"],
    test_suite = 'tests.suite',
    )
