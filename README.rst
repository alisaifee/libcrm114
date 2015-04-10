.. |travis-ci| image:: https://secure.travis-ci.org/alisaifee/limits.png?branch=master
    :target: https://travis-ci.org/#!/alisaifee/limits?branch=master

From http://crm114.sourceforge.net/wiki/doku.php?id=download:

*************************
CRM114 C-callable Library
*************************

|travis-ci|

This is the callable library version of CRM114. It has most of the
classifiers as the standalone language (with some significant
improvements- one alpha tester says they saw a 10x speedup in their
application). This version is LGPLed (Library GPL) so you can link it
with your own code, whether open-source or proprietary. You still need
TRE (on Fedora, “yum install tre-devel”). Note that with improvements
come costs: libcrm114 classifiers are NOT compatible with standalone
CRM114 class files (necessary, because libcrm114 classifiers can work
even on systems that don't have filesystems, like embedded
processors). The code is now pretty stable and the API solidly
entrenched by use in several real products, so the api is unlikely to
change in unpleasant ways.

Advantages of libcrm114: It's much faster; everything is
in-memory. You can call everything directly from ANSI C. Because
everything is in memory, it's good for embedded systems where you
don't _have_ a unix-style file system to talk to. No arcane language
to learn, it's all just ANSI C. You can export classifiers as ASCII
“CSV-like” format so trained classifiers are 32/64-bit portable and
cross-platform Linux/Mac/Windows portable (the internal binary
classifier format is still tied to a particular architecture, but
that's never exported any more).

Disadvantages of libcrm114: Not all classifiers are currently
supported (in particular, Neural Net, Correllator, OSBF, and Winnow
are NOT yet supported). There's no crazy language, so you need to get
your data into memory on your own. You still need TRE. You do pay a
(not horrible) startup cost loading a classifier from a an ASCII
CSV-like file, but since you can then reuse the classifier for as many
documents as you want, in the long term this cost is amortized down to
zero and you get significant speedup.


Dependencies
============

Debian/Ubuntu: ``sudo apt-get install libtre5 libtre-dev``

OS X: ``brew install tre``

Building
========

.. code-block:: bash

  python setup.py build
