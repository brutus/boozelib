.. boozelib documentation master file, created by
   sphinx-quickstart on Tue Apr 17 20:25:45 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========
boozelib
========

A Python module containing a couple of functions to calculate the
*blood alcohol content* of people.

It's at home at GitHub: https://github.com/brutus/boozelib/

Contents
========

.. toctree::
   :maxdepth: 2
   
   install
   functions
   formulas

Functions
=========

The two main functions are:

.. autofunction:: boozelib.get_bac
   :noindex:

.. autofunction:: boozelib.get_degradation
   :noindex:

You can browse the full :doc:`documentation<functions>` online. Or you can get
help with ``pydoc boozelib``, if you already got **boozelib** installed.

Examples
--------

>>> from boozelib import get_bac, get_degradation
>>> get_bac(32, 96, 186, False, 500, 4.9)
0.28773587455687716
>>> get_bac(32, 48, 162, True, 500, 4.9)
0.5480779730398769
>>> get_degradation(32, 96, 186, False, 60)
0.21139778538872606
>>> get_degradation(32, 48, 162, True, 60)
0.20133476560648536

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.

If you find any bugs, issues or anything, please use the `issue tracker`_ on
GitHub.

.. _`issue tracker`: https://github.com/brutus/boozelib/issues/
