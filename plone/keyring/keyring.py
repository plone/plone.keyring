import random

from persistent.list import PersistentList
from zope.interface import implements
from zope.location.interfaces import IContained

from plone.keyring.interfaces import IKeyring

def GenerateSecret(length=64):
    secret=""
    for i in range(length):
        secret+=chr(random.getrandbits(8))

    return secret


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
            self[i]=None

    def rotate(self):
        self.pop()
        self.insert(0, GenerateSecret())

    @property
    def current(self):
        return self.data[0]





