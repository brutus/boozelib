# boozelib

**VERSION**: `0.7.0`

A Python module containing a couple of tools to calculate the
**blood alcohol content** of people.

It's at home at GitHub: <https://github.com/brutus/boozelib/>.

As a side note: I created this library mainly to have a very simple module to
try different Python testing and packaging best practice. _This is in no way a
serious medical approach and also accepts a rather big level of abstraction._
Depending on your use case, this might be okay; but I would not deem it fit for
serious health and / or legal stuff 😉 🍻

# Install

You can install it from [PyPi], it is known as `boozelib` and has no
dependencies:

```shell
pip install --user boozelib
```

# Usage

The two main functions are:

-   `get_blood_alcohol_content(age, weight, height, sex, volume, percent)`

    Return the **blood alcohol contents** raise (per mill) for a person after a
    drink.

    Given a drink containing _volume_ (ml) of _percent_ (vol/vol) alcohol, for a
    person with _age_ (years), _weight_ (kg) and _height_ (cm) — using a
    formular for "female body types" if _sex_ is true.

-   `get_blood_alcohol_degradation(age, weight, height, sex, minutes=1, degradation=None)`

    Return the **alcohol degradation** (per mill) for a person over _minutes_.

    For a person with _age_ (years), _weight_ (kg) and _height_ (cm), using the
    formular for "female body types" if _sex_ is true, over the given _minutes_.
    If _degradation_ is not set, `ALCOHOL_DEGRADATION` is used as default.

This uses some constants and one variable you might want to review:

-   `ALCOHOL_DEGRADATION`: the default value for alcohol degradation; meaning
    the amount of alcohol (in gram) your body is degrading per minute, per
    kilogram body weight. This is usually a value between `0.0017` and `0.0025`
    (about 0.1—0.2 per thousand per hour).

## Examples

Return the **blood alcohol contents** raise (per mill) for a person after a
drink:

```python
from boozelib import get_blood_alcohol_content

get_blood_alcohol_content(
	age=32, weight=48, height=162, sex=True, volume=500, percent=4.9
)
# ⇒ 0.5480779730398769
```

And to calculate alcohol degradation:

```python
from boozelib import get_blood_alcohol_degradation

get_blood_alcohol_degradation(
	age=32, weight=48, height=162, sex=True, minutes=60
)
# ⇒ 0.20133476560648536
```

You can change the default for _alcohol degradation_ globally via setting
`boozelib.ALCOHOL_DEGRADATION`. Or change the value for _alcohol degradation_
per call:

```python
get_blood_alcohol_degradation(
	age=32, weight=48, height=162, sex=True, minutes=60, degradation=0.002
)
# ⇒ 0.16106781248518828
```

# Documentation

See the source or the [documentation] for more information and the used
[formulas].

# Development Setup

[Poetry] is used to manage a _virtual environment_ for the development setup.

A `Makefile` is provided, that collects some common tasks. You have to run
the following **once**, to setup your environment:

```shell
make setup
```

# Testing

[nox] is used as a test runner (with [ward] as the framework). If you have the
_development environment_ activated, you can just run:

```shell
make tests
```

If something fails, please get in touch.

# Thanks and Contributions

-   Big hugs to Mathilda for hanging around and helping me figuring out all
    that math and biology stuff.

If you find bugs, issues or anything else, please use the [issue tracker] on
GitHub. Issues and PRs are welcome ❤️

[documentation]: https://boozelib.readthedocs.org/
[formulas]: https://boozelib.readthedocs.org/en/latest/background.html
[issue tracker]: https://github.com/brutus/boozelib/issues
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pypi]: https://pypi.org/project/BoozeLib/
[ward]: https://wardpy.com/
