Used Formulas
=============

Note: The following documentation of the used formulars is in german... Sorry,
but I'm too laszy to translate them right now. ``:(`` Google around
**Widmark** and **Watson** for starters.

Wir errechnen die Blut Alkohol Konzentration (BAK) in Gramm pro Kilogramm.

Variablen und Konstanten
------------------------

| ``pa`` = Dichte von Alkohols (g/ml) = 0.8
| ``pb`` = Dichte von Blut (g/cm\ :sup:`3`) = 1.055
| ``w`` = Anteil von Wasser im Blut (%) = 0.8
|
| ``v`` = Volumen des Getraenks (ml)
| ``e`` = Alkoholanteil des Getraenks (:sup:`v`/:sub:`v`)
|
| ``t`` = Alter in Jahren
| ``h`` = Groesse in cm
| ``m`` = Gewicht in kg

Widmark-Formel
--------------

Blut Alkohol Konzentration (BAK) => **c**

``c = A / (m * r)``

Aufgenommene Masse des Alkohols in Gramm => **A**

``A = V * e * pa``

Reduktionsfaktor => **r**

* male: ``r = 0,7``
* female: ``r = 0,6``

Watson-Ergaenzung
~~~~~~~~~~~~~~~~~

Reduktionsfaktor => **r**

``r = (pb * kw) / (w * m)``

Gesamtkoerperwasser (nach Geschlecht) => **kw**

* male ``kw = 2,447 - (0,09516 * t) + (0,1074 * h) + (0,3362 * m)``
* female ``kw = 0,203 - (0,07 * t)    + (0,1069 * h) + (0,2466 * m)``

Zusammengefasst
~~~~~~~~~~~~~~~

``c = (pa * v * e * w) / (pb * kw)``

Finale Formel
~~~~~~~~~~~~~

* male: ``(pa * v * e * w) / (pb * (2,447 - (0,09516 * t) + (0,1074 * h) + (0,3362 * m)))``

* female: ``(pa * v * e * w) / (pb * (0,203 - (0,07 * t)    + (0,1069 * h) + (0,2466 * m)))``

Alcohol degradation
-------------------

Average is 0.15 g/kg per hour (0.0025 per minute).
