# boozelib

**VERSION**: `0.5.0`

A Python module containing a couple of tools to calculate the
**blood alcohol content** of people.

It's at home at GitHub: <https://github.com/brutus/boozelib/>.

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

-   `get_blood_alcohol_degradation(age, weight, height, sex, minutes=1)`

    Return the **alcohol degradation** (per mill) for a person over _minutes_.

    For a person with _age_ (years), _weight_ (kg) and _height_ (cm), over the
    given _minutes_ — using a formular for "female body types" if _sex_ is true.

## Examples

```python
>>> from boozelib import get_blood_alcohol_content

>>> get_blood_alcohol_content(
>>> ... age=32, weight=96, height=186, sex=False, volume=500, percent=4.9
>>> ... )
>>> 0.28773587455687716

>>> get_blood_alcohol_content(
>>> ... age=32, weight=48, height=162, sex=True, volume=500, percent=4.9
>>> ... )
>>> 0.5480779730398769

>>> from boozelib import get_blood_alcohol_degradation

>>> get_blood_alcohol_degradation(
>>> ... age=32, weight=96, height=186, sex=False, minutes=60
>>> ... )
>>> 0.21139778538872606

>>> get_blood_alcohol_degradation(
>>> ... age=32, weight=48, height=162, sex=True, minutes=60
>>> ... )
>>> 0.20133476560648536
```

## Documentation

See the source or the [documentation] for more information and the used
[formulas].

# Testing

[nox] is used as a test runner (with [pytest] as the framework). So you need
to have `nox` installed, before you can run the test suit like this:

```shell
nox
```

If you already have the _development environment_ activated (see below), you
can skip the install and just run:

```shell
make tests
```

If something fails, please get in touch.

# Development Setup

[pipenv] is used to manage a _virtual environment_ for the development setup.

A `Makefile` is provided, that collects some common tasks. You have to run
the following **once**, to setup your environment:

```shell
make setup
```

# Thanks and Contributions

-   Big hugs to Mathilda for hanging around and helping me figuring out all
    that math and biology stuff.

If you find bugs, issues or anything else, please use the [issue tracker] on
GitHub. Issues and PRs are welcome ❤️

[documentation]: https://boozelib.readthedocs.org/
[formulas]: https://boozelib.readthedocs.org/en/latest/background.html
[issue tracker]: https://github.com/brutus/boozelib/issues
[nox]: https://nox.thea.codes/
[pipenv]: https://pipenv.pypa.io/
[pypi]: https://pypi.org/project/BoozeLib/
[pytest]: https://docs.pytest.org/
