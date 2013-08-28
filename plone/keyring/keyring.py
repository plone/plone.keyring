from random import choice

from persistent.list import PersistentList
from zope.interface import implements
from zope.location.interfaces import IContained

from plone.keyring.interfaces import IKeyring
from plone.keyring import django_random


def GenerateSecret(length=64):
    return django_random.get_random_string(length)


class Keyring(PersistentList):

    implements(IKeyring, IContained)

    __parent__ = __name__ = None

    def __init__(self, size=5):
        PersistentList.__init__(self)
        for i in range(size):
            self.append(None)

    def __iter__(self):
        for item in self.data:
            yield item

    def clear(self):
        for i in range(len(self)):
            self[i] = None

    def rotate(self):
        self.pop()
        self.insert(0, GenerateSecret())

    def fill(self):
        """
        add missing keys
        """
        for i in range(len(self)):
            key = self[i]
            if key is None:
                self[i] = GenerateSecret()

    @property
    def current(self):
        return self.data[0]

    def random(self):
        return choice([k for k in self.data if k])
