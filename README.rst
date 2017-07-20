.. image:: https://img.shields.io/pypi/v/scrolls.svg
   :target: https://pypi.python.org/pypi/scrolls
.. image:: https://img.shields.io/travis/ilogue/scrolls.svg
   :target: https://travis-ci.org/ilogue/scrolls
.. image:: https://codeclimate.com/github/ilogue/scrolls/badges/coverage.svg
   :target: https://codeclimate.com/github/ilogue/scrolls/coverage
   :alt: Test Coverage
.. image:: https://codeclimate.com/github/ilogue/scrolls/badges/gpa.svg
   :target: https://codeclimate.com/github/ilogue/scrolls
   :alt: Code Climate
.. image:: https://readthedocs.org/projects/scrolls/badge/?version=latest
   :target: http://scrolls.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

=======
scrolls
=======

Simple log management


Install scrolls::

  pip install scrolls

Configure a client system to forward log events to scrolls::

  scrolls configure --server my.scrolls-server.org

Start listening to log events::

  scrolls listen

Launch web app to view log messages from a browser::

  scrolls serve
  
  
Features
========

- Browse events by application or host
- Limit access to the web app by password

