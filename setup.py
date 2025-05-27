from setuptools import setup, find_packages

setup(
    name="challengeforge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "networkx",
        "PyYAML"
    ],
    entry_points={
        "console_scripts": [
            "challengeforge=challengeforge.cli:app",
        ],
    },
    author="Your Name",
    description="CLI toolkit for generating and packaging coding challenges",
)
