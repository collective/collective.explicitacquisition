Changelog
=========

2.1 (unreleased)
----------------

- Redirect to first site root when you have multiple sites in the path.
  This avoids rendering parts of site2, including using its language and navigation, when you access url site1/site2.
  [maurits]


2.0 (2021-02-05)
----------------

- Update package (black, isort, structure) [jensens]

- Drop support of Python 2.7, [jensens]

- Support Python 3 on Plone 5.2.x+
  [spereverde]


1.1 (2015-02-18)
----------------

- Add MANIFEST.in and fix release.
  [thet]


1.0 (2015-02-17)
----------------

- Fix issue where a user could access an unintended object through
  acquisition magic. See https://dev.plone.org/ticket/13793.
  [gotcha]
