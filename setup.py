# -*- coding: UTF-8 -*
"""
Setup script for behave.example

USAGE:
    python setup.py install
    python setup.py behave_test     # -- XFAIL on Windows (currently).
"""

import sys
import os.path

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, os.path.abspath(HERE))

from setuptools import find_packages, setup
# -- PREPARED: from setuptools_behave import behave_test


# -----------------------------------------------------------------------------
# CONFIGURATION:
# -----------------------------------------------------------------------------
description = """\
    Aplicación de TDD y ATDD al clásico juego del ahorcado.
"""

# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="ahorcado",
    version="1.2.7",
    url="https://github.com/agustindangelo/ahorcado-tdd",
    author="Agustín D'Angelo",
    author_email="dangeloagustinariel@gmail.com",
    license="BSD",
    description= description,
    keywords   = "utility",
    platforms  = [ 'any' ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[
        "behave>=1.2.6",
        "PyHamcrest>=1.9",
        "parse>=1.8.2",
        "parse_type>=0.4.2",
        "six>=1.11.0",
    ],
    include_package_data= True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: behave",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
        "Topic :: Documentation",
        "Topic :: Education",
    ],
    packages=find_packages('src'),
    zip_safe = True,
)
