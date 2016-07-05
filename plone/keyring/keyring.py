import time
from random import choice

from persistent.list import PersistentList
from zope.interface import implementer
from zope.location.interfaces import IContained

from plone.keyring.interfaces import IKeyring
from plone.keyring import django_random


def GenerateSecret(length=64):
    return django_random.get_random_string(length)


@implementer(IKeyring, IContained)
class Keyring(PersistentList):

    __parent__ = __name__ = None

    last_rotation = 0

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
        self.last_rotation = time.time()

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
        """
        since we could be on a rotation boundary,
        only rotate one less than the total
        """
        keys = self.data
        if len(keys) > 1:
            keys = keys[:-1]
        return choice([k for k in keys if k])
