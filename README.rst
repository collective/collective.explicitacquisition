collective.explicitacquisition
==============================

.. image:: https://github.com/collective/collective.explicitacquisition/workflows/Testing/badge.svg
    :target: https://github.com/collective/collective.explicitacquisition/actions?query=workflow%3ATesting


Access to acquired content in CMF/ Plone should not be allowed.

This package disables content acquisition.

Installation
============

Add the package to your `buildout`'s instances `eggs` section.
Once the ZCML is loaded by Zope it is active.
No further steps needed.


Source Code
===========

The sources are in a GIT DVCS with its main branches at
`github <https://github.com/collective/collective.explicitacquisition>`_.

We'd be happy to see many forks and pull-requests to make collective.explicitacquisition even better.


Contributors
============

This package is a repackaging of Godfroid Chapelle's (`gotcha <https://github.com/gotcha>`_) Products.CMFPlone branch "publication through explicit acquisition"_, which solves ticket 13793 (references old, archived bug tracker).

Further contributors:

- Johannes Raggam (`thetet <https://github.com/thet>`_)
- Kim Paulissen (`spereverde <https://github.com/spereverde>`_
- Maik Derstappen (`MrTango <https://github.com/MrTango>`_)
- Jens Klein (`jensens <https://github.com/jensens>`_)
