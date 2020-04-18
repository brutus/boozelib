========
boozelib
========

**VERSION**: ``0.5.0``

A Python module containing a couple of tools to calculate the *blood alcohol
content* of people.

It's at home at GitHub: https://github.com/brutus/boozelib/

Install
=======

You can install it from `PyPi`_, it is known as ``boozelib`` and has no
dependencies::

    pip install --user boozelib

Usage
=====

The two main functions are:

* ``get_blood_alcohol_content(age, weight, height, sex, volume, percent)``

  Returns the **Blood Alcohol Content** (raise) for a person (described by the
  given attributes) after a drink containing *volume* ml of alcohol with the
  given *percent* (vol/vol).

* ``get_degradation(age, weight, height, sex, minutes)``

  Returns the **alcohol degradation** (per mill) of a person with the given
  stats in the given number of *minutes*.

See the `documentation`_ for more information and other probably helpful stuff.
If you're interested in the used formulas, see the source or browse the
formulas_ online (maybe easier to read).

Examples
--------

>>> from boozelib import get_blood_alcohol_content

>>> get_blood_alcohol_content(
...   age=32, weight=96, height=186, sex=False, volume=500, percent=4.9
... )
0.28773587455687716

>>> get_blood_alcohol_content(
...   age=32, weight=48, height=162, sex=True, volume=500, percent=4.9
... )
0.5480779730398769

>>> from boozelib import get_degradation

>>> get_degradation(age=32, weight=96, height=186, sex=False, minutes=60)
0.21139778538872606

>>> get_degradation(age=32, weight=48, height=162, sex=True, minutes=60)
0.20133476560648536

Testing
=======

`nox`_ is used as a test runner (with `pytest`_ as the framework). So you need
to have ``nox`` installed, before you can run the test suit like this::

    nox

If you already have the *development environment* activated (see below), you
can skip the install and just run::

    make tests

If something fails, please get in touch.

Development Setup
=================

`pipenv`_ is used to manage a *virtual environment* for the development setup.

A ``Makefile`` is provided, that collects some common tasks. You have to run
the following **once**, to setup your environment::

    make setup

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.

If you find any bugs, issues or anything, please use the `issue tracker`_ on
GitHub - issues and PRs are welcome <3

.. _`documentation`: https://boozelib.readthedocs.org/
.. _`formulas`: https://boozelib.readthedocs.org/en/latest/background.html
.. _`issue tracker`: https://github.com/brutus/boozelib/issues
.. _`nox`: https://nox.thea.codes/
.. _`pipenv`: https://pipenv.pypa.io/
.. _`pypi`: https://pypi.org/project/BoozeLib/
.. _`pytest`: https://docs.pytest.org/
