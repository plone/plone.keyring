from persistent.mapping import PersistentMapping
from zope.container.sample import SampleContainer
from zope.interface import implements

from plone.keyring.interfaces import IKeyManager
from plone.keyring.keyring import Keyring


class KeyManager(SampleContainer):
    implements(IKeyManager)

    def __init__(self):
        SampleContainer.__init__(self)

        self[u"_system"] = Keyring()
        self[u"_system"].fill()

        # to be used with anonymous users
        self[u'_anon'] = Keyring()
        self[u'_anon'].fill()

        # to be used with forms, plone.protect here..
        self[u'_forms'] = Keyring()
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
