from persistent.mapping import PersistentMapping
from plone.keyring.interfaces import IKeyManager
from plone.keyring.keyring import Keyring
from zope.container.sample import SampleContainer
from zope.interface import implementer


@implementer(IKeyManager)
class KeyManager(SampleContainer):
    def __init__(self, keyring_size=5):
        SampleContainer.__init__(self)

        if keyring_size < 1:
            keyring_size = 5  # prevent not having any keys

        self["_system"] = Keyring(keyring_size)
        self["_system"].fill()

        # to be used with anonymous users
        self["_anon"] = Keyring(keyring_size)
        self["_anon"].fill()

        # to be used with forms, plone.protect here..
        self["_forms"] = Keyring(keyring_size)
        self["_forms"].fill()

    def _newContainerData(self):
        return PersistentMapping()

    def clear(self, ring="_system"):
        if ring is None:
            for ring in self.values():
                ring.clear()
        else:
            self[ring].clear()

    def rotate(self, ring="_system"):
        if ring is None:
            for ring in self.values():
                ring.rotate()
        else:
            self[ring].rotate()

    def secret(self, ring="_system"):
        return self[ring].current
