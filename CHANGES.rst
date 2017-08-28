Changelog
=========


3.0.2 (2017-08-27)
------------------

Fixes:

- Use zope.interface decorator.
  [gforcada]


3.0.1 (2015-05-11)
------------------

- Minor cleanup: whitespace, git ignores.
  [gforcada, rnix]


3.0.0 (2014-04-13)
------------------

- use more default keyrings and be able to select random key from ring
  [vangheem]


2.0.1 (2012-12-15)
------------------

- Use system random when available. This is part of the fix for
  https://plone.org/products/plone/security/advisories/20121106/24
  [davisagli]

- Add MANIFEST.in.
  [WouterVH]


2.0 - 2010-07-18
----------------

- Update package information.
  [hannosch]


2.0b1 - 2010-06-13
------------------

- Added a meta.zcml to load the GenericSetup ZCML if installed.
  [hannosch]

- Update license to BSD following board decision.
  Cfr. http://lists.plone.org/pipermail/membership/2009-August/001038.html
  [elro]


2.0a1 - 2009-11-13
------------------

- Updated to use `zope.container` instead of `zope.app.container`.
  [hannosch]

- Specify package dependencies.
  [hannosch]


1.2 - 2008-05-08
----------------

- Fix registration of the GenericSetup profile.
  [witsch]


1.1 - 2008-05-02
----------------

- Add an optional GenericSetup profile to register the KeyManager as utility.
  Required for plone.keyring on Plone 3.0.
  [mj]


1.0 - 2008-04-21
----------------

- No changes.
  [wichert]


1.0b1 - 2008-03-07
------------------

- Tweak the tests to better test the API.
  [witsch]


1.0a1 - 2008-01-22
------------------

- Initial release.
  [wichert]
