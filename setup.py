#!/usr/bin/env python

__author__ = "Joel Pedraza"
__copyright__ = "Copyright 2014, Joel Pedraza"
__license__ = "MIT"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='hibget',
      version='0.0.1',
      description='Humble Indie Bundle Downloader',
      author='Joel Pedraza',
      author_email='joel@joelpedraza.com',
      url='https://github.com/saik0/hibget',
      install_requires=['requests >= 2.0.0', 'appdirs'],
      packages=['hibget'],
      scripts=['hibget/hibget.py']
     )