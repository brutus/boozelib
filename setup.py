from distutils.core import setup

setup(
  name='BoozeLib',
  version='0.3',
  author='Brutus',
  author_email='brutus.dmc@googlemail.com',
  description='A Python module containing a couple of functions to '\
    'calculate the *blood alcohol content* of people.',
  long_description=open('README.rst').read(),
  url='https://github.com/brutus/boozelib',
  download_url='https://github.com/brutus/boozelib/zipball/master',
  license='LICENSE.txt',
  classifiers=['License :: OSI Approved :: GNU General Public License (GPL)'],
  py_modules=['boozelib/boozelib', 'boozelib/test/boozelib_test'],
)
