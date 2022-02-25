#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GSMA ESO rule-based extraction",
    version="0.0.1",
    author="Deeper Insights",
    description="A python skeleton",
    packages=setuptools.find_packages(),
    scripts=['bin/example.py'],
    python_requires='>=3',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
