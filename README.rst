========
boozelib
========

A Python module containing a couple of functions to calculate blood alcohol
levels, along with some helper-stuff, a wrapper function and two classes.

Functions
=========

* ``get_bac(age, weight, height, sex, volume, percent)``

  Returns the *Blood Alcohol Level* (raise) for a person (described by the
  given attributes) after a drink containing *volume* ml of alcohol with the
  given *percent* (vol/vol).

* ``get_degradation(age, weight, height, sex, minutes)``

  Returns the amount of alcohol (per mill) that a person with the given 
  stats degenerates in x *minutes*.

See the documentattion inside the source file (``init.py``)
for more information.

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.
