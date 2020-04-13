=========
Changelog
=========

All notable changes to this project will be documented in this file. The format
is based on `Keep a Changelog`_, and this project adheres to
`Semantic Versioning`_.

You can find the issue tracker at <https://github.com/brutus/boozelib/issues>.

.. _keep a changelog: https://keepachangelog.com/en/1.0.0/
.. _semantic versioning: https://semver.org/spec/v2.0.0.html

.. towncrier release notes start

0.4.1 (2020-04-13)
==================

Features
--------

- Manage development requirements in a *virtual environment* with `pipenv <https://github.com/pypa/pipen>`_.
- Handle version bumps with `bump2version <https://github.com/c4urself/bump2version>`_.
- Use `towncrier <https://github.com/twisted/towncrier>`_ for tracking changes.

Changes
-------

- Converted ``CHANGES.rst`` to ``CHANGELOG.rst``.

0.4 (2012-04-18)
================

Features
--------

- Generate documentation with ``sphinx``.
- Added support for `readthedocs.org`_.


0.3 (2012-04-17)
================

Features
--------

- Added support for ``distutils``.


0.2 (2012-04-15)
================

Changes
-------

- Refactored the code to *calculate* and *convert* utility functions as well as
  ``get_bac`` and ``get_degradation`` for the main work.


Deprecations and Removals
-------------------------

- Removed the ``User`` and ``Drink`` classes.


0.1.3 (2012-04-14)
==================

Bugfixes
--------

- Prevent the *blood alcohol levels* from getting ``< 0``.


0.1.2 (2012-04-12)
==================

Bugfixes
--------

- Fixed some typos in the docs.


0.1.1 (2012-04-10)
==================

Bugfixes
--------

- Fixed some typos in both classes.


0.1 (2012-04-07)
================

Features
--------

- Initial release 🎉
