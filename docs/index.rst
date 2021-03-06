========
boozelib
========

A Python module containing a couple of functions to calculate the
**blood alcohol content** of people.

It's at home at https://github.com/brutus/boozelib/

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

   install
   modul
   background

Install
=======

You can install it from `PyPi`_, it is known as ``boozelib`` and has no
dependencies::

    pip install --user boozelib

Global Variables
================

This uses some constants and one variable you might want to review:

- :data:`ALCOHOL_DEGRADATION`: the default value for alcohol degradation;
  meaning the amount of alcohol (in gram) your body is degrading per minute, per
  kilogram body weight. This is usually a value between ``0.0017`` and
  ``0.0025`` (about 0.1—0.2 per thousand per hour).

Functions
=========

The two main functions are:

.. autofunction:: boozelib.get_blood_alcohol_content
   :noindex:

.. autofunction:: boozelib.get_blood_alcohol_degradation
   :noindex:

Examples
--------

Return the **blood alcohol contents** raise (per mill) for a person after a
drink:

>>> get_blood_alcohol_content(
...     age=32, weight=96, height=186, sex=False, volume=500, percent=4.9
... )
0.28773587455687716

>>> get_blood_alcohol_content(
...     age=32, weight=48, height=162, sex=True, volume=500, percent=4.9
... )
0.5480779730398769

And to calculate alcohol degradation:

>>> get_blood_alcohol_degradation(
...     age=32, weight=96, height=186, sex=False, minutes=60
... )
0.21139778538872606

>>> get_blood_alcohol_degradation(
...     age=32, weight=48, height=162, sex=True, minutes=60
... )
0.20133476560648536

You can change the default for *alcohol degradation* globally via setting
:data:`ALCOHOL_DEGRADATION`. Or change the value for *alcohol degradation* per
call:

>>> get_blood_alcohol_degradation(
...     age=32, weight=48, height=162, sex=True, minutes=60, degradation=0.002
... )
0.16106781248518828

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.

If you find any bugs, issues or anything, please use the `issue tracker`_ on
GitHub.

.. include:: includes/links.rst
