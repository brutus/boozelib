"""boozelib

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

Wrapper & Classes
-----------------

There is also a wrapper function ``get_new_bak(user, drink=None, minutes=0,
bac=0)``, that relies on the two provided classes: ``user`` and ``drink``:

  Note: The two included classes are just for convenience, you can use
        **any** class, as long as the needed attributes are present.

  *user* needs to have the following attributes:
    - age (in years, integer)
    - height (in cm, integer)
    - weight (in kg, integer)
    - sex (male = False, female = True)
    - bac (optional, integer)

  *drink* needs to have the following attributes:
    - volume (volume of the beverage: in ml, integer)
    - percent (parts of alcohol in the beverage: in volume percent, integer)


Benutzte Formeln
================

Note: The following documentation of the used formulars is in german;
      sorry, but I'm too laszy to translate them right now.
      Google around 'Widmark' and 'Watson' for starters.

Wir errechnen die Blut Alkohol Konzentration (BAK) in Gramm pro Kilogramm.

Variablen und Konstanten
------------------------

  pa = Dichte von Alkohols (g/ml) = 0.8
  pb = Dichte von Blut (g/cm^3) = 1.055
   w = Anteil von Wasser im Blut (%) = 0.8

   v = Volumen des Getraenks (ml)
   e = Alkoholanteil des Getraenks (v/v)

   t = Alter in Jahren
   h = Groesse in cm
   m = Gewicht in kg

Widmark-Formel
--------------

  Blut Alkohol Konzentration (BAK) => **c**

  ``c = A / (m * r)``

  Aufgenommene Masse des Alkohols in Gramm => **A**

  ``A = V * e * pa``

  Reduktionsfaktor => **r**

  r (male) = 0,7
  r (female) = 0,6

Watson-Ergaenzung
~~~~~~~~~~~~~~~~~

  Reduktionsfaktor => **r**

  r = (pb * kw) / (w * m)

  Gesamtkoerperwasser (nach Geschlecht) => **kw**

  kw (male)   = 2,447 - (0,09516 * t) + (0,1074 * h) + (0,3362 * m)
  kw (female) = 0,203 - (0,07 * t)    + (0,1069 * h) + (0,2466 * m)

Zusammengefasst
~~~~~~~~~~~~~~~

  BAK = (pa * v * e * w) / (pb * kw)

Finale Formel
~~~~~~~~~~~~~

female =

 (pa * v * e * w) / (pb * (0,203 - (0,07 * t)    + (0,1069 * h) + (0,2466 * m)))

male =

 (pa * v * e * w) / (pb * (2,447 - (0,09516 * t) + (0,1074 * h) + (0,3362 * m)))

Alcohol degradation
-------------------

Average is 0.15 g/kg per hour (0.0025 per minute).

Thanks and Contributions
========================

* Big hugs to Mathilda for hanging around and helping me figuring out all
  that math and biology stuff.

"""

__version__ = '0.1'
__author__  = 'Brutus [DMC] <brutus.dmc@googlemail.com>'
__license__ = 'GNU General Public License v3 or above - '\
              'http://www.opensource.org/licenses/gpl-3.0.html'


__all__ = (
  'get_bac', 'get_degradation', 'get_blood_alcohol', 'degrade_bac',
  'User', 'Drink'
)


PA = 0.8 # density of alcohol (g/ml)
PB = 1.055 # density of blood (g/cm^3)
W = 0.8 # parts of water in blood (%)


class User(object):

  def __init__(self, age, weight, height, sex, name=None):
    self.age = int(age)
    self.weight = int(weight)
    self.height = int(height)
    self.sex = bool(sex) # female = True
    self.name = str(name)
    self.bac = 0

  def __repr__(self):
    return "<User({0.age}, {0.weight}, {0.height}, {0.sex}, {0.name})>".format(self)

  def __str__(self):
    return "[{0.name}] {0.age} years, {0.weight} kg, {0.height} cm ({1}): {0.bac}".format(
      self, 'female' if self.sex else 'male'
    )

  def drink(self, drink, minutes=0):
    self.bac += get_bac(
      self.age, self.weight, self.height, self.sex,
      drink.volume, drink.percent
    )
    if minutes:
      self.wait(minutes)

  def wait(self, minutes):
    self.bac -= get_degradation(
      self.age, self.weight, self.height, self.sex,
      minutes
    )

  def as_list(self):
    return [self.age, self.weight, self.height, self.sex, self.name]


class Drink(object):

  def __init__(self, volume, percent, name=None):
    self.volume = int(volume) # in ml
    self.percent = float(percent)
    self.name = str(name)

  def __repr__(self):
    return "<Drink({0.volume}, {0.percent}, {0.name})".format(self)

  def __str__(self):
    return "[{0.name}] Volumen: {0.volume}, Percent: {0.percent}".format(self)

  def as_list(self):
    return [self.volume, self.percent, self.name]


def calculate_alcohol(volume, percent):
  """Return the amount of alcohol (in gramm) contained in a drink"""
  return PA * volume * (percent / 100) # A

def calculate_degradation(weight, minutes):
  """Return the ammount of alcohl (in gramm) that a body with the given
     weight degenerates in the given *minutes*
  """
  return 0.0025 * weight * minutes

def calculate_bw(age, weight, height, sex):
  """Returns the amount of water (in liter) in a persons body"""
  if sex: # female
    return 0.203 - (0.07 * age) + (0.1069 * height) + (0.2466 * weight)
  else: # male
    return 2.447 - (0.09516 * age) + (0.1074 * height) + (0.3362 * weight)

def promille_to_gramm(bac, age, weight, height, sex):
  """Return the amount of alcohol (in gramm) for a person with the given
     body stats and blood alcohol concentration (per mill)
  """
  bw = calculate_bw(age, weight, height, sex)
  return (bac * (PB * bw)) / W

def gramm_to_promille(gramm, age, weight, height, sex):
  """Return the blood alcohol concentration (per mill) for a person with the
     given body stats and amount of alcohol (in gramm) in blood
  """
  bw = calculate_bw(age, weight, height, sex)
  return (gramm * W) / (PB * bw)


def get_bac(age, weight, height, sex, volume, percent):
  """Return the blood alcohol concentration (per mill) after a given drink."""
  return gramm_to_promille(
    calculate_alcohol(volume, percent),
    age, weight, height, sex
  )

def get_degradation(age, weight, height, sex, minutes):
  """Return the ammount of alcohl (in per mill) that a body with given stats
     degenerates in the given *minutes*
  """
  return gramm_to_promille(
    calculate_degradation(weight, minutes),
    age, weight, height, sex
  )

def degrade_bac(age, weight, height, sex, bac, minutes):
  """Returns the new blood alcohol level (per mill) after *minutes*"""
  alc_old = promille_to_gramm(bac, age, weight, height, sex)
  alc_new = alc_old - calculate_degradation(weight, minutes)
  return gramm_to_promille(alc_new, age, weight, height, sex)


def get_blood_alcohol(user, drink=None, minutes=0, bac=0):
  """Returns blood alcohol concentration in (per mill).
     Takes previous bac and time passed into account.

    Utillity function for use with ``user`` and ``drink`` objects

  """
  if minutes and bac > 0:
    bac -= get_degradation(
      user.age, user.weight, user.height, user.sex,
      minutes
    )
  if drink:
    bac += get_bac(
      user.age, user.weight, user.height, user.sex,
      drink.volume, drink.percent
    )
  return bac
