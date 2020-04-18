""" Calculate blood alcohol content.

Functions to calculate the **blood alcohol content** of people.

Functions
=========

The two main functions are:

* ``get_blood_alcohol_content(age, weight, height, sex, volume, percent)``

  Returns the **Blood Alcohol Content** (raise) for a person with the given
  stats after a drink containing *volume* ml of alcohol with the given *percent*
  (vol/vol).

* ``get_degradation(age, weight, height, sex, minutes)``

  Returns the **alcohol degradation** (per mill) of a person with the given
  stats in the given number of *minutes*.

Examples
--------

>>> get_blood_alcohol_content(
...     age=32, weight=96, height=186, sex=False, volume=500, percent=4.9
... )
0.28773587455687716

>>> get_blood_alcohol_content(
...     age=32, weight=48, height=162, sex=True, volume=500, percent=4.9
... )
0.5480779730398769

>>> get_degradation(age=32, weight=96, height=186, sex=False, minutes=60)
0.21139778538872606

>>> get_degradation(age=32, weight=48, height=162, sex=True, minutes=60)
0.20133476560648536

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all that
  math and biology stuff.

If you find any bugs, issues or anything, please use the `issue tracker`_ on
GitHub.

.. _`issue tracker`: https://github.com/brutus/boozelib/issues

"""

__version__ = "0.5.0"
__author__ = "Brutus [DMC] <brutus.dmc@googlemail.com>"
__license__ = (
    "GNU General Public License v3 or above - "
    "http://www.opensource.org/licenses/gpl-3.0.html"
)


__all__ = (
    "calculate_alcohol",
    "calculate_body_water",
    "calculate_bw",
    "calculate_degradation",
    "get_bac",
    "get_blood_alcohol_content",
    "get_degradation",
    "gramm_to_promille",
    "promille_to_gramm",
)


PA = 0.8  #: density of alcohol (g/ml)
PB = 1.055  #: density of blood (g/cm^3)
W = 0.8  #: parts of water in blood (%)


def calculate_alcohol(volume, percent):
    """ Return the amount of alcohol (in gramm) contained in a drink. """
    return PA * volume * (percent / 100)


def calculate_degradation(weight, minutes):
    """ Return alcohol degeneration (in gramm) over the given *minutes*. """
    return 0.0025 * weight * minutes


def calculate_body_water(age, weight, height, sex):
    """ Return the amount of water (in liter) in a persons body. """
    if sex:  # female
        return 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
    else:  # male
        return 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)


calculate_bw = calculate_body_water  # for compatibillity (<0.4.2)


def promille_to_gramm(promille, age, weight, height, sex):
    """ Return the *amount of alcohol* (in gramm) given *promille* and body stats.

    For a person with the given body stats and *blood alcohol contents*
    (per mill).

    """
    bw = calculate_body_water(age, weight, height, sex)
    return (promille * (PB * bw)) / W


def gramm_to_promille(gramm, age, weight, height, sex):
    """ Return the *blood alcohol contents* (per mill) given alcohol and body stats.

    For a person with the given body stats with an amount of alcohol (in gramm)
    in the blood.

    """
    bw = calculate_body_water(age, weight, height, sex)
    return (gramm * W) / (PB * bw)


def get_blood_alcohol_content(age, weight, height, sex, volume, percent):
    """ Return the *blood alcohol contents* raise (per mill) for person after drink.

    For a person with the given body stats, affected by a drink containing
    *volume* (ml) of alcohol with the given *percent* (vol/vol).

    """
    return gramm_to_promille(
        calculate_alcohol(volume, percent), age, weight, height, sex
    )


get_bac = get_blood_alcohol_content  # for compatibillity (<0.4.2)


def get_degradation(age, weight, height, sex, minutes):
    """ Returns the *alcohol degradation* (per mill) for *person* over *minutes*.

    For a person with the given body stats, over the given *minutes*.

    """
    return gramm_to_promille(
        calculate_degradation(weight, minutes), age, weight, height, sex
    )
