.. |travis-ci| image:: https://img.shields.io/travis/alisaifee/pycrm114/master.svg?style=flat-square
    :target: https://travis-ci.org/#!/alisaifee/pycrm114?branch=master
.. |coveralls| image:: https://img.shields.io/coveralls/alisaifee/limits/master.svg?style=flat-square
    :target: https://coveralls.io/r/alisaifee/pycrm114?branch=master
.. |pypi| image:: https://img.shields.io/pypi/v/pycrm114.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycrm114
.. |license| image:: https://img.shields.io/pypi/l/pycrm114.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycrm114/
.. _crm114: http://crm114.sourceforge.net/wiki/doku.php

|travis-ci| |coveralls| |pypi|

********
pycrm114
********

Pythonic bindings for `crm114`_

CRM114 - the Controllable Regex Mutilator
=========================================

    CRM114 is a system to examine incoming e-mail, system log streams, data files or other
    data streams, and to sort, filter, or alter the incoming files or data streams according
    to the user's wildest desires.

    -- crm114.sourceforge.net


Quickstart
==========

No persistence
--------------
.. code-block:: python

    import pycrm114

    crm = pycrm114.CRM114(classes=["spam", "ham"])
    crm.learn("spam", "foo bar")
    crm.learn("ham", "bar is good")
    assert crm.classify("is bar good")["class"] == "ham"
    assert crm.classify("foo bar good")["class"] == "spam"
    crm.forget("spam", "foo bar")
    assert crm.classify("foo bar good")["class"] == "ham"


File System Persistence
-----------------------

.. code-block:: python

    import pycrm114

    crm = pycrm114.CRM114(
        classes=["spam", "ham"],
        storage=pycrm114.storage.FileSystemStorage("/var/tmp/crm-test")
    )
    crm.learn("spam", "foo bar")
    crm.learn("ham", "bar is good")
    crm.save()
    new_crm = pycrm114.CRM114(
        classes=["spam", "ham"],
        storage=pycrm114.storage.FileSystemStorage("/var/tmp/crm-test")
    )
    assert new_crm.classify("is bar good")["class"] == "ham"
    assert new_crm.classify("foo bar good")["class"] == "spam"

Dependencies
============

Debian/Ubuntu: ``sudo apt-get install libtre5 libtre-dev``

OS X: ``brew install tre``

Tests
=====

Dependencies
------------

.. code-block:: bash 

  pip install -r requirements/test.txt

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

* `crm114`_ 

