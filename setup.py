# -*- coding: utf-8 -*-

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(here,'LICENSE'), encoding='utf-8') as f:
    license = f.read()

setup(
    name='lockss-stf',
    version='1.0.0',
    url='https://github.com/lockss/lockss-stf.git',
    license=license,
    author='LOCKSS-DLSS, Stanford University',
    author_email='clairetg@stanford.edu',
    description='The LOCKSS Stochastic Testing Framework',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['docs', 'bin']),
    python_requires='>=2.7'
)
