========
boozelib
========

A Python module containing a couple of functions to calculate blood alcohol
levels, along with some helper-stuff, a wrapper function and two classes.

It's at home at GitHub: https://github.com/brutus/boozelib/

**Dependencies**

*boozelib* has no dependencies. If you want to run the included test cases
you need the nose_ testing framework though (see below).

Functions
=========

The two main functions are:

* ``get_bac(age, weight, height, sex, volume, percent)``

  Returns the *Blood Alcohol Content* (raise) for a person (described
  by the given attributes) after a drink containing *volume* ml of alcohol
  with the given *percent* (vol/vol).

* ``get_degradation(age, weight, height, sex, minutes)``

  Returns the amount of alcohol (per mill) that a person with the given
  stats degenerates in x *minutes*.

See the documentation inside the source file (``__init__.py``) for more
information and other probably helpful stuff.

Testing
=======

If you find any bugs, issues or anything use the `issue tracker`_ on GitHub.

If you want to run the test cases, see that you got the needed dependencies
installed and run ``nosetests`` from the main directory (the one containing
this file). If something fails, please get in touch.

Install nose
------------

You can install nose_ with pip_ "a tool for installing and managing Python
packages": ``sudo pip install nose`` or trough your OS package management, eg:
``sudo apt-get install python-nose`` or the like.

If you don't have pip_ installed, you can get it with two commands:

  ``$ sudo curl http://python-distribute.org/distribute_setup.py | python``

  ``$ sudo curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python``

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.

.. _nose: http://readthedocs.org/docs/nose/en/latest/testing.html
.. _pip: http://www.pip-installer.org/en/latest/index.html
.. _`issue tracker`: https://github.com/brutus/boozelib/issues
