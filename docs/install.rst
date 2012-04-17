Install
=======

You can install **boozelib** with pip_ or from source.

Install with pip
----------------

pip_ is "*a tool for installing and managing Python packages*". If you have it
installed, simply get **boozelib** like this:

Install system wide:

  ``sudo pip install boozelib``

Install only for the current user:

  ``pip install --user boozelib``

Install pip
~~~~~~~~~~~

If you don't have pip_ installed yet, you can get it with these two commands:

  ``$ sudo curl http://python-distribute.org/distribute_setup.py | python``

  ``$ sudo curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python``

Install from source
-------------------

You can fetch the latest sourceball_ from github and unpack it, or just clone
the repository: ``git clone git://github.com/brutus/boozelib.git``. If you got
the source, change into the directory and use ``setup.py``:

Install system wide:

  ``sudo python setup.py install``

Install only for the current user:

  ``python setup.py install --user``

Testing
=======

There are some doctes in the module, you can run them from the ``boozelib``
directory by either running the module by itself ``python boozelib.py`` or
running ``python -m doctest -v boozelib.py``.

If you want to run the test cases, see that you got nose_ installed and run
``nosetests`` from the ``boozelib`` directory (the one containing the module).
If you got **boozelib** already installed, run them like this: ``nosetest
test_boozelib``

If something fails, please get in touch.

Install nose
------------

You can install nose_ with pip_ ``sudo pip install nose`` or propably also
trough your OS package management, eg: ``sudo apt-get install python-nose`` or
the like.

.. _nose: http://readthedocs.org/docs/nose/en/latest/testing.html
.. _pip: http://www.pip-installer.org/en/latest/index.html
.. _sourceball: https://github.com/brutus/boozelib/zipball/master
