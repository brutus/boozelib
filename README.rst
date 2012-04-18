========
boozelib
========

A Python module containing a couple of functions to calculate the
*blood alcohol content* of people.

It's at home at GitHub: https://github.com/brutus/boozelib/

**boozelib** has no dependencies. If you want to run the included test cases
you need the nose_ testing framework though (see below).

Functions
=========

The two main functions are:

* ``get_bac(age, weight, height, sex, volume, percent)``

  Returns the *Blood Alcohol Content* (raise) for a person (described by the
  given attributes) after a drink containing *volume* ml of alcohol with the
  given *percent* (vol/vol).

* ``get_degradation(age, weight, height, sex, minutes)``

  Returns the *alcohol degradation* (per mill) of a person with the given
  stats in the given number of *minutes*.

See the documentation inside the source file (``boozelib.py``) for more
information and other probably helpful stuff. You can browse the full
documentation_ online, there is also a quick overview_ of all available
constants and functions. Or you can get help with ``pydoc boozelib``, if you
already got **boozelib** installed.

If you're interested in the used formulas, see the source and documentation or
browse the formulas_ online (maybe easier to read).

Examples
--------

>>> get_bac(32, 96, 186, False, 500, 4.9)
0.28773587455687716

>>> get_bac(32, 48, 162, True, 500, 4.9)
0.5480779730398769

>>> get_degradation(32, 96, 186, False, 60)
0.21139778538872606

>>> get_degradation(32, 48, 162, True, 60)
0.20133476560648536

Install
=======

You can install **boozelib** with pip_ or from source.

Install with pip
----------------

pip_ is "*a tool for installing and managing Python packages*". If you have it
installed, simply get **boozelib** like this:

Install system wide:

  ``sudo pip install boozelib``

Install only for the current user:

  ``pip install --user boozelib``

Install pip
~~~~~~~~~~~

If you don't have pip_ installed yet, you can get it with these two commands:

  ``$ sudo curl http://python-distribute.org/distribute_setup.py | python``

  ``$ sudo curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python``

Install from source
-------------------

You can fetch the latest sourceball_ from github and unpack it, or just clone
the repository: ``git clone git://github.com/brutus/boozelib.git``. If you got
the source, change into the directory and use ``setup.py``:

Install system wide:

  ``sudo python setup.py install``

Install only for the current user:

  ``python setup.py install --user``

Testing
=======

There are some doctes in the module, you can run them from the ``boozelib``
directory by either running the module by itself ``python boozelib.py`` or
running ``python -m doctest -v boozelib.py``.

If you want to run the test cases, see that you got nose_ installed and run
``nosetests`` from the ``boozelib`` directory (the one containing the module).
If you got **boozelib** already installed, run them like this: ``nosetest
test_boozelib``

If something fails, please get in touch.

Install nose
------------

You can install nose_ with pip_ ``sudo pip install nose`` or propably also
trough your OS package management, eg: ``sudo apt-get install python-nose`` or
the like.

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.

If you find any bugs, issues or anything, please use the `issue tracker`_ on
GitHub.

.. _documentation: http://boozelib.readthedocs.org/
.. _overview: http://boozelib.readthedocs.org/en/latest/functions.html
.. _formulas: http://boozelib.readthedocs.org/en/latest/formulas.html
.. _`issue tracker`: https://github.com/brutus/boozelib/issues
.. _sourceball: https://github.com/brutus/boozelib/zipball/master
.. _nose: http://readthedocs.org/docs/nose/en/latest/testing.html
.. _pip: http://www.pip-installer.org/en/latest/index.html
