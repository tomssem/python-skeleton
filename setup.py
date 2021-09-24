#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_skeleton", # Replace with your own name
    version="0.0.1",
    author="Some Person",
    author_email="someone@example.com",
    description="A python skeleton",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshbressers/python-skeleton",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
