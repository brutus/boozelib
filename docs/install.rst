=====
Setup
=====

You can install it from `PyPi`_, it is known as ``boozelib`` and has no
dependencies::

    pip install --user boozelib

Development Setup
=================

`pipenv`_ is used to manage a *virtual environment* for the development setup.

A ``Makefile`` is provided, that collects some common tasks. You have to run
the following **once**, to setup your environment::

    make setup

Testing
=======

`nox`_ is used as a test runner (with `pytest`_ as the framework). So you need
to have ``nox`` installed, before you can run the test suit like this::

    nox

If you already have the *development environment* activated (see below), you
can skip the install and just run::

    make tests

If something fails, please get in touch.

.. include:: includes/links.rst
