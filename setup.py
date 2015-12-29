from setuptools import setup, find_packages

with open('README.rst') as f:
    desc = f.read()

setup(
    name = "spdx",
    version = "2.3.0-beta.1",
    packages = find_packages(),
    author = "Brendan Molloy",
    author_email = "brendan+pypi@bbqsrc.net",
    description = "SPDX license list database",
    license = "CC0-1.0",
    keywords = ["spdx", "licenses", "database"],
    url = "https://github.com/bbqsrc/spdx-python",
    long_description=desc,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
