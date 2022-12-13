#!/usr/bin/env python

from setuptools import setup, find_packages
from os import environ

with open('requirements.txt') as fp:
    install_requires = fp.read()

with open('requirements_test.txt') as fp:
    tests_require = fp.read()

setup(name='example-cli',
      version=environ.get('EXAMPLE_CLI_VERSION', '0.0.1'),
      description='Example CLI',
      author='Adrian Galera',
      author_email='',
      python_requires='>=3.6.*',
      packages=find_packages(),
      install_requires=install_requires,
      tests_require=tests_require,
      entry_points={
          'console_scripts': [
              'example-cli = examplecli.entrypoint:start',
          ]
      }
      )
