from persistent.mapping import PersistentMapping
from zope.container.sample import SampleContainer
from zope.interface import implementer

from plone.keyring.interfaces import IKeyManager
from plone.keyring.keyring import Keyring


@implementer(IKeyManager)
class KeyManager(SampleContainer):

    def __init__(self, keyring_size=5):
        SampleContainer.__init__(self)

        if keyring_size < 1:
            keyring_size = 5  # prevent not having any keys

        self[u"_system"] = Keyring(keyring_size)
        self[u"_system"].fill()

        # to be used with anonymous users
        self[u'_anon'] = Keyring(keyring_size)
        self[u'_anon'].fill()

        # to be used with forms, plone.protect here..
        self[u'_forms'] = Keyring(keyring_size)
        self[u'_forms'].fill()

    def _newContainerData(self):
        return PersistentMapping()

    def clear(self, ring=u"_system"):
        if ring is None:
            for ring in self.values():
                ring.clear()
        else:
            self[ring].clear()

    def rotate(self, ring=u"_system"):
        if ring is None:
            for ring in self.values():
                ring.rotate()
        else:
            self[ring].rotate()

    def secret(self, ring=u"_system"):
        return self[ring].current
