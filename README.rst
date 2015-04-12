.. |travis-ci| image:: https://secure.travis-ci.org/alisaifee/limits.png?branch=master
    :target: https://travis-ci.org/#!/alisaifee/limits?branch=master

|travis-ci|

********
pycrm114
********

Python bindings for libcrm114


Dependencies
============

Debian/Ubuntu: ``sudo apt-get install libtre5 libtre-dev``

OS X: ``brew install tre``

Tests
=====

Dependencies
------------

.. code-block:: bash 

  pip install tox nose

To test against different python versions use tox::
  
  tox 

To run the tests with the active python::

  python setup.py build && nosetests tests 


Building
========

.. code-block:: bash

  python setup.py build

References
==========

* `crm114 <http://crm114.sourceforge.net/wiki/doku.php>`_

