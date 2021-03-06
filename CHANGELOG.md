# Changelog

All notable changes to this project will be documented in this file. The format
is based on [Keep a Changelog][], and this project adheres to
[Semantic Versioning][].

You can find the **issue tracker** at:
<https://github.com/brutus/boozelib/issues>

[keep a changelog]: https://keepachangelog.com/
[semantic versioning]: https://semver.org/

<!-- TOWNCRIER -->

## 0.7.0 (2021-03-08)

### Features

- ➕ Added `sphinx-autobuild` for doc generation.
- ✨ Add optional argument **degradation** to the
  `calculate_alcohol_degradation` and `get_blood_alcohol_degradation`
  functions.

  If set, this value is used for _alcohol degradation_ instead of the
  `ALCOHOL_DEGRADATION` module level variable.

### Deprecations and Removals

- In the next version the value used for _alcohol degradation_ will be lowered.

  To keep the current default, you can override `ALCOHOL_DEGRADATION`, or use
  the new **degradation** argument to the `calculate_alcohol_degradation` and
  `get_blood_alcohol_degradation` functions.


## 0.6.0 (2021-02-02)

### Features

- Added Python [type hints](https://docs.python.org/3/library/typing.html).
- Use [mypy](https://mypy.readthedocs.io/) to check type hints.

### Changes

- Renamed the used constants (use decriptive names).
- Ported the README to markdown.
- Switched to [Poetry](https://python-poetry.org/) for packaging (from
  [Pipenv](https://github.com/pypa/pipenv)).
- Only accept keyword-arguments for all functions (not positional ones).
- Switch back to [ward](https://wardpy.com/) as test framework.
- Translated the background section in the docs.
- Rename `calculate_alcohol` to `calculate_alcohol_weight`,
  `calculate_degradation` to `calculate_alcohol_degradation` and
  `get_degradation` to `get_blood_alcohol_degradation`.
- Unified function signatures.

### Deprecations and Removals

- Remove deprecated function names (`calculate_bw` and `get_bac`).
- Remove support for Python `==2.7`.


# 0.5.0 (2020-04-18)

This will be the **last version** supporting Python `2.7`.

## Features

-   Test all supported Python versions (`>=2.7`).
-   Add configuration for [Read the Docs](https://readthedocs.org/).

## Changes

-   Use [pytest](https://docs.pytest.org/) instead of [ward](https://wardpy.com/)
    (mostly to check Python 2.7).

# 0.4.2 (2020-04-14)

## Features

-   Added `Makefile` to collect and document common development tasks.
-   Use [flakehell](https://github.com/life4/flakehell),
    [black](https://github.com/psf/black) and
    [reorder-python-imports](https://github.com/asottile/reorder_python_imports)
    for linting.
-   Add git-hooks for linting via [pre-commit](https://pre-commit.com/).
-   Use [flit](https://flit.readthedocs.io/) for packaging.
-   Use [nox](https://nox.thea.codes/) and [ward](https://wardpy.com/) as test
    runners.
-   Add [Sphinx](https://www.sphinx-doc.org/) to development setup and update it.

## Changes

-   Updated the README.
-   Made git ignore basic Python stuff.
-   Move tests to `tests/`.
-   Moved module source to `src/` directory.

## Deprecations and Removals

-   Remove docs generated by _Sphinx_.

## Bugfixes

-   Track `__version__` in source with
    [bump2version](https://github.com/c4urself/bump2version).

    # 0.4.1 (2020-04-13)

## Features

-   Manage development requirements in a _virtual environment_ with
    [pipenv](https://github.com/pypa/pipen).
-   Handle version bumps with
    [bump2version](https://github.com/c4urself/bump2version).
-   Use [towncrier](https://github.com/twisted/towncrier) for tracking changes.

## Changes

-   Converted `CHANGES.rst` to `CHANGELOG.rst`.

    # 0.4 (2012-04-18)

## Features

-   Generate documentation with [Sphinx](https://www.sphinx-doc.org/).
-   Added support for [readthedocs.org](https://readthedocs.org).

    # 0.3 (2012-04-17)

## Features

-   Added support for `distutils`.

    # 0.2 (2012-04-15)

## Changes

-   Refactored the code to _calculate_ and _convert_ utility functions as well as
    `get_bac` and `get_degradation` for the main work.

## Deprecations and Removals

-   Removed the `User` and `Drink` classes.

    # 0.1.3 (2012-04-14)

## Bugfixes

-   Prevent the _blood alcohol levels_ from getting `< 0`.

    # 0.1.2 (2012-04-12)

## Bugfixes

-   Fixed some typos in the docs.

    # 0.1.1 (2012-04-10)

## Bugfixes

-   Fixed some typos in both classes.

    # 0.1 (2012-04-07)

## Features

-   Initial release 🎉
