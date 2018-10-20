from setuptools import find_packages, setup

setup(
    name="beckonjira",
    version="1.0.0",
    description="Beckon Jira Helper",
    author="Mo Kweon",
    author_email="Kyung.Kweon@beckon.com",
    url="https://github.com/beckon",
    packages=find_packages(),
    scripts=["scripts/beckon-jira"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    license="MIT",
)
