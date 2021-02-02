Used Formulas
=============

We used the formulars from **Widmark** and **Watson** — with the modification
by **Eicker** (for the female blood alcohol content) — to calcualte the
*blood alcohol content* and *alcohol degradation* in this module.

Variables and Constants
-----------------------

| ``pa`` = Density of alcohol (g/ml) = 0.8
| ``pb`` = Density of blood (g/ml) = 1.055
| ``w`` = Parts water in blood (%) = 0.8
|
| ``v`` = Volume of the drink (ml)
| ``e`` = Alcohol concentration in the drink (:sup:`v`/:sub:`v`)
|
| ``t`` = Age (in years)
| ``h`` = Height (in cm)
| ``m`` = Weight (in kg)

Widmark-Formel
--------------

Blood Alcohol Concentration (BAC) => **c**

``c = A / (m * r)``

Mass of alcohol intake (in gramm) => **A**

``A = V * e * pa``

Factor for alcohol degradation *"Reduktionsfaktor"* (by sex) => **r**

* male: ``r = 0,7``
* female: ``r = 0,6``

Watson-Addition
~~~~~~~~~~~~~~~

*Reduktionsfaktor* => **r**

``r = (pb * kw) / (w * m)``

Water in the body (by sex) => **kw**

* male ``kw = 2,447 - (0,09516 * t) + (0,1074 * h) + (0,3362 * m)``
* female ``kw = 0,203 - (0,07 * t)    + (0,1069 * h) + (0,2466 * m)``

Combined
~~~~~~~~

``c = (pa * v * e * w) / (pb * kw)``

Final Formel
~~~~~~~~~~~~

* male: ``(pa * v * e * w) / (pb * (2,447 - (0,09516 * t) + (0,1074 * h) + (0,3362 * m)))``

* female: ``(pa * v * e * w) / (pb * (0,203 - (0,07 * t)    + (0,1069 * h) + (0,2466 * m)))``

Alcohol degradation
-------------------

Average is 0.15 g/kg per hour (0.0025 per minute).
