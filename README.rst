.. -*- coding: utf-8 -*-

.. image:: https://github.com/gforcada/flake8-plone-hasattr/actions/workflows/testing.yml/badge.svg?branch=master
   :target: https://github.com/gforcada/flake8-plone-hasattr/actions/workflows/testing.yml

.. image:: https://coveralls.io/repos/gforcada/flake8-plone-hasattr/badge.svg?branch=master
   :target: https://coveralls.io/github/gforcada/flake8-plone-hasattr?branch=master

Flake8 Plone hasattr plugin
===========================
Python standard ``hasattr`` is considered harmful (within Plone projects).

The (hidden) problem with ``hasattr`` is that it swallows exceptions,
which in your normal business logic you really don't want to.

Specially in Plone context that could mean swallowing a database error,
or a permission exception, etc.

Take, for instance, the following code:

.. code-block:: python

    >>> class Foo(object):
    ...     @property
    ...     def my_attr(self):
    ...         raise ValueError('nope, nope, nope')
    ...
    >>> bar = Foo()
    >>> bar.my_attr
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in my_attr
    ValueError: nope, nope, nope
    >>> hasattr(Foo, 'my_attr')
    True
    >>> hasattr(bar, 'my_attr')
    False

One should rather do:

.. code-block:: python

    >>> getattr(bar, 'my_attr', None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in my_attr
    ValueError: nope, nope, nope

Or in case you want to handle an exception:

.. code-block:: python

    >>> try:
    ...     value = getattr(bar, 'my_attr', None)
    ... exception ValueError:
    ...     value = None

This plugin is based on a python checker that was in `plone.recipe.codeanalysis`_.

Install
-------
Install with pip:

.. code-block:: console

    $ pip install flake8-plone-hasattr

Requirements
------------
- Python 3.8, 3.9, 3.10, 3.11 and pypy3
- flake8

License
-------
GPL 2.0

.. _`plone.recipe.codeanalysis`: https://pypi.python.org/pypi/plone.recipe.codeanalysis
