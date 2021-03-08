""" Calculate blood alcohol content.

Functions to calculate the **blood alcohol content** of people.

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

- ``get_blood_alcohol_content(age, weight, height, sex, volume, percent)``

    Return the **blood alcohol contents** raise (per mill) for a person after a
    drink.

    Given a drink containing *volume* (ml) of alcohol with the *percent*
    (vol/vol), for a person with *age* (years), *weight* (kg) and *height* (cm),
    using the formular for "female body types" if *sex* is true.

- ``get_blood_alcohol_degradation(
        age, weight, height, sex, minutes=1, degradation=None,
    )``

    Return the alcohol degradation (per mill) for a person over *minutes*.

    For a person with *age* (years), *weight* (kg) and *height* (cm), using the
    formular for "female body types" if *sex* is true, over the given *minutes*.
    If *degradation* is not set, :data:`ALCOHOL_DEGRADATION` is used as default.

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

* Big hugs to Mathilda for hanging around and helping me figuring out all that
  math and biology stuff.

If you find any bugs, issues or anything, please use the `issue tracker`_ on
GitHub.

.. _`issue tracker`: https://github.com/brutus/boozelib/issues

"""
import warnings
from typing import Optional

__version__ = "0.7.0"
__author__ = "Brutus [DMC] <brutus.dmc@googlemail.com>"
__license__ = (
    "GNU General Public License v3 or above - "
    "http://www.opensource.org/licenses/gpl-3.0.html"
)


__all__ = (
    "calculate_alcohol_degradation",
    "calculate_alcohol_weight",
    "calculate_body_water",
    "get_blood_alcohol_content",
    "get_blood_alcohol_degradation",
    "gramm_to_promille",
    "promille_to_gramm",
)


ALCOHOL_DENSITY: float = 0.8  #: density of alcohol (g/ml)
BLOOD_DENSITY: float = 1.055  #: density of blood (g/ml)
WATER_IN_BLOOD: float = 0.8  #: parts of water in blood (%)
ALCOHOL_DEGRADATION: float = 0.0025  #: for kg body weight per minute (g)

ALCOHOL_DEGRADATION_WARNING = """
In the next version the value used for alcohol degradation will be lowered. To
keep the current default, you can override `ALCOHOL_DEGRADATION`, or use the new
*degradation* argument to the `calculate_alcohol_degradation` and
`get_blood_alcohol_degradation` functions.
"""


def calculate_alcohol_weight(*, volume: int, percent: float) -> float:
    """Return the amount of alcohol (in gramm) contained in a drink.

    Given a drink with a *volume* (ml) containing *percent* (vol/vol) alcohol.

    """
    return ALCOHOL_DENSITY * volume * (percent / 100)


def calculate_alcohol_degradation(
    *, weight: int, minutes: int = 1, degradation: Optional[float] = None
) -> float:
    """Return the alcohol degeneration (in gramm) over time.

    For a person with *weight* (in kg) over the given *minutes*. If
    *degradation* is not set, :data:`ALCOHOL_DEGRADATION` is used as default.

    """
    warnings.warn(ALCOHOL_DEGRADATION_WARNING, DeprecationWarning)
    if degradation is None:
        degradation = ALCOHOL_DEGRADATION
    return degradation * weight * minutes


def calculate_body_water(*, age: int, weight: int, height: int, sex: bool) -> float:
    """Return the amount of water (in liter) in a persons body.

    For a person with *age* (years), *weight* (kg) and *height* (cm), using
    the formular for "female body types" if *sex* is true.

    """
    if sex:  # female
        return 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
    else:  # male
        return 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)


def promille_to_gramm(*, promille: float, body_water: float) -> float:
    """Return the ammount of alcohol in a persons body (in gramm), given *promille*
    and *body water* (in liter).

    """
    return (promille * (BLOOD_DENSITY * body_water)) / WATER_IN_BLOOD


def gramm_to_promille(*, gramm: float, body_water: float) -> float:
    """Return the blood alcohol contents of a person, given alcohol (in *gramm*)
    and *body water* (in liter).

    """
    return (gramm * WATER_IN_BLOOD) / (BLOOD_DENSITY * body_water)


def get_blood_alcohol_content(
    *,
    age: int,
    weight: int,
    height: int,
    sex: bool,
    volume: int,
    percent: float,
) -> float:
    """Return the blood alcohol contents raise (per mill) for a person after a drink.

    Given a drink containing *volume* (ml) of alcohol with the *percent*
    (vol/vol), for a person with *age* (years), *weight* (kg) and *height* (cm),
    using the formular for "female body types" if *sex* is true.

    """
    gramm = calculate_alcohol_weight(volume=volume, percent=percent)
    body_water = calculate_body_water(age=age, weight=weight, height=height, sex=sex)
    return gramm_to_promille(gramm=gramm, body_water=body_water)


def get_blood_alcohol_degradation(
    *,
    age: int,
    weight: int,
    height: int,
    sex: bool,
    minutes: int = 1,
    degradation: Optional[float] = None,
) -> float:
    """Return the alcohol degradation (per mill) for a person over *minutes*.

    For a person with *age* (years), *weight* (kg) and *height* (cm), using the
    formular for "female body types" if *sex* is true, over the given *minutes*.
    If *degradation* is not set, :data:`ALCOHOL_DEGRADATION` is used as default.

    """
    warnings.warn(ALCOHOL_DEGRADATION_WARNING, DeprecationWarning)
    if degradation is None:
        degradation = ALCOHOL_DEGRADATION
    gramm = calculate_alcohol_degradation(
        weight=weight, minutes=minutes, degradation=degradation
    )
    body_water = calculate_body_water(age=age, weight=weight, height=height, sex=sex)
    return gramm_to_promille(gramm=gramm, body_water=body_water)
