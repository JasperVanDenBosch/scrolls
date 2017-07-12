.. image:: https://img.shields.io/pypi/v/scrolls.svg
   :target: https://pypi.python.org/pypi/scrolls
.. image:: https://img.shields.io/travis/rust-lang/rust.svg
   :target: https://travis-ci.org/ilogue/scrolls
.. image:: https://codeclimate.com/github/codeclimate/codeclimate/badges/coverage.svg
   :target: https://codeclimate.com/github/codeclimate/codeclimate/coverage
   :alt: Test Coverage
.. image:: https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg
   :target: https://codeclimate.com/github/codeclimate/codeclimate
   :alt: Code Climate


scrolls
=======

Simple log management


Install scrolls::

  pip install scrolls


Configure the system to forward log events::

  scrolls configure --server my.scrolls-server.org


Start listening to log events::

  scrolls listen


Launch web app to view log messages from a browser::

  scrolls serve

