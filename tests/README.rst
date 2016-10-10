Unit Tests
==========

This directory contains unit tests (of webstr framework itself) written in
pytest_ framework.

.. _pytest: http://docs.pytest.org/en/latest/goodpractices.html

Unit Test Execution
-------------------

One can run the tests via pytest directly, which is useful when one needs to
specify additional parameters to pytest, eg.::

    $ py.test-3 -x --pdb tests

Via ``setup.py``::

    $ python3 setup.py test

Or via tox, which will run the tests under both python2 and pytnon3 (good for
CI purposes)::

    $ tox
