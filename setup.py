#!/usr/bin/env python


from distutils.core import setup


# Read long description; README
with open('README.md', 'r') as readme_file:
    README_TEXT = readme_file.read()


# Setup
setup(name='algozoo',
      version='0.1',
      description='Basic Algorithms and Data Structures',
      long_description=README_TEXT,
      author='Yannis Liapis',
      author_email='yliapis44@gmail.com',
      url='https://github.com/yliapis/algozoo',
      packages=['algozoo'],
     )
