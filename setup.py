import os
import sys
from typing import List

from setuptools import Command, find_packages, setup


class Format(Command):
    user_options: List[str] = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        err_isort = os.system("isort --recursive  setup.py scripts src -y")
        err_black = os.system("black .")
        sys.exit(err_isort or err_black)


setup(
    name="beckonjira",
    version="1.0.0",
    description="Beckon Jira Helper",
    author="Mo Kweon",
    author_email="Kyung.Kweon@beckon.com",
    url="https://github.com/kkweon/beckonjira",
    package_dir={"": "src"},
    packages=find_packages("src", exclude="beckonjira.egg-info"),
    setup_requires=["pytest-runner", "pytest-pylint", "pytest-black", "pytest-mypy"],
    cmdclass={"format": Format},
    tests_require=["pytest", "pylint", "black", "mypy"],
    install_requires=["boto3", "requests"],
    license="MIT",
    entry_points={"console_scripts": ["beckon-jira = beckonjira.__init__:main"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
)
