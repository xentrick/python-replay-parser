#!/usr/bin/env python
# coding: utf-8
from setuptools import find_packages, setup

from replay_parser import VERSION

setup(
    name="rocket-league-replay-parser",
    version=".".join(str(n) for n in VERSION),
    url="https://github.com/xentrick/rocket-league-replay-parser",
    author="Nick Mavis",
    author_email="itsnick@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    description="Parser for Rocket League replay files.",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
