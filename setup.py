#!/usr/bin/env python


from setuptools import find_packages, setup


# Read long description; README
with open('README.md', 'r') as readme_file:
    README_TEXT = readme_file.read()


# Setup
setup(name='algozoo',
      version='0.1',
      description='Classic Algorithms and Data Structures',
      long_description=README_TEXT,
      author='Yannis Liapis',
      author_email='yliapis44@gmail.com',
      url='https://github.com/yliapis/algozoo',
      packages=find_packages(exclude=['tests']),
      )
