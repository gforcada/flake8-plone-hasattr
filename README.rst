.. -*- coding: utf-8 -*-

.. image:: https://travis-ci.org/gforcada/flake8-plone-hasattr.svg?branch=master
   :target: https://travis-ci.org/gforcada/flake8-plone-hasattr

.. image:: https://coveralls.io/repos/gforcada/flake8-plone-hasattr/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/gforcada/flake8-plone-hasattr?branch=master

Flake8 Plone hasattr plugin
===========================
Python standard ``hasattr`` is considered harmful (within Plone projects).

The (hidden) problem with ``hasattr`` is that it swallows exceptions,
which in your normal business logic you really don't want to.

Specially in Plone context that could mean swallowing a database error,
or a permission exception, etc.

Install
-------
Install with pip::

    $ pip install flake8-plone-hasattr

Requirements
------------
- Python 2.7, 3.3, 3.4
- flake8

License
-------
GPL 2.0
