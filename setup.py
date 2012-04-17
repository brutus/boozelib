# -*- coding: UTF-8 -*-

from distutils.core import setup


setup(
  name='BoozeLib',
  version=open('CHANGES.txt').readline().split()[0][1:-1],
  author='Brutus',
  author_email='brutus.dmc@googlemail.com',
  description='A Python module containing a couple of functions to '\
    'calculate the *blood alcohol content* of people.',
  long_description=open('README.rst').read(),
  url='https://github.com/brutus/boozelib',
  download_url='https://github.com/brutus/boozelib/zipball/master',
  license='LICENSE.txt',
  classifiers=['License :: OSI Approved :: GNU General Public License (GPL)'],
  package_dir = {'': 'boozelib'},
  py_modules=['boozelib', 'test_boozelib'],
)
