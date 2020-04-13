""" Calculate blood alcohol content.

A Python module containing a couple of functions to calculate the
*blood alcohol content* of people.

Functions
=========

The two main functions are:

* ``get_bac(age, weight, height, sex, volume, percent)``

  Returns the **Blood Alcohol Content** (raise) for a person (described by the
  given attributes) after a drink containing *volume* ml of alcohol with the
  given *percent* (vol/vol).

* ``get_degradation(age, weight, height, sex, minutes)``

  Returns the **amount of alcohol (per mill)** that a person with the given
  stats degenerates in the given number of *minutes*.

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

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.

If you find any bugs, issues or anything, please use the
`issue tracker`_ on GitHub.

.. _`issue tracker`: https://github.com/brutus/boozelib/issues

"""

__version__ = '0.4'
__author__  = 'Brutus [DMC] <brutus.dmc@googlemail.com>'
__license__ = 'GNU General Public License v3 or above - '\
              'http://www.opensource.org/licenses/gpl-3.0.html'


__all__ = (
  'get_bac', 'get_degradation',
  'calculate_alcohol', 'calculate_degradation', 'calculate_bw',
  'gramm_to_promille', 'promille_to_gramm'
)


PA = 0.8 #: density of alcohol (g/ml)
PB = 1.055 #: density of blood (g/cm^3)
W = 0.8 #: parts of water in blood (%)


def calculate_alcohol(volume, percent):
  """Return the amount of alcohol (in gramm) contained in a drink"""
  return PA * volume * (percent / 100) # A

def calculate_degradation(weight, minutes):
  """Return the ammount of alcohl (in gramm) that a body with the given
     weight degenerates in the given *minutes*
  """
  return 0.0025 * weight * minutes

def calculate_bw(age, weight, height, sex):
  """Return the amount of water (in liter) in a persons body"""
  if sex: # female
    return 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
  else: # male
    return 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)

def promille_to_gramm(bac, age, weight, height, sex):
  """Return the amount of alcohol (in gramm) for a person with the given
     body stats and blood alcohol content (per mill)
  """
  bw = calculate_bw(age, weight, height, sex)
  return (bac * (PB * bw)) / W

def gramm_to_promille(gramm, age, weight, height, sex):
  """Return the blood alcohol content (per mill) for a person with the
     given body stats and amount of alcohol (in gramm) in blood
  """
  bw = calculate_bw(age, weight, height, sex)
  return (gramm * W) / (PB * bw)


def get_bac(age, weight, height, sex, volume, percent):
  """Returns the *Blood Alcohol Content* (raise) for a person (described by
     the given attributes) after a drink containing *volume* ml of alcohol with
     the given *percent* (vol/vol).
  """
  return gramm_to_promille(
    calculate_alcohol(volume, percent),
    age, weight, height, sex
  )


def get_degradation(age, weight, height, sex, minutes):
  """Returns the *alcohol degradation* (per mill) of a person with the given
     stats in the given number of *minutes*.
  """
  return gramm_to_promille(
    calculate_degradation(weight, minutes),
    age, weight, height, sex
  )


if __name__ == '__main__':
  import doctest
  doctest.testmod()
