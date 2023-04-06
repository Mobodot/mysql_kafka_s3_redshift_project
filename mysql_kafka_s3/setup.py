from setuptools import setup, find_packages

__VERSION__ = "0.0.0"
PROJECT_NAME = "e_shopping"
AUTHOR_NAME = "Mobdot"
AUTHOR_EMAIL = "mobosomto@gmail.com"
DESCRIPTION = "A data migration project to move data from \
    mysql to s3 using pyspark, mysql and kafka"

setup(
    name=PROJECT_NAME,
    version=__VERSION__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages()
)