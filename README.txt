Introduction
============

*plone.keyring* contains a Zope utility that facilitates handling of
secrets in an application. Secrets are very important in modern applications,
which is why a shared tool to manage them is useful.

plone.keyring contains two basic components:

* a *keyring*: a data structures which contains one or more secrets.

* a *key manager*: a utility which contains the available keyrings and
  provides some convenience methods to manage them


Keyrings
========

The keyring is the workhorse: it contains a set of secrets for a specific
purpose. A ring has room for a fixed number of secrets which is set at
creation time. The most recently added secret is considered to be the
`current` secret and the one that should be used. Older secrets in the ring
can be used to keep data generated with older secrets valid for a period of
time.

Key manager
===========

The key manager is a container for the available keyrings. It always
contains a default system keyring which is used when no other ring is
explicitly requested.

Installation
============

You'll need to register a KeyManager as a persistent utility. On Zope2 with
GenericSetup, this can be done by loading the included profile.
