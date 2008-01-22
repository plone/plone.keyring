import types
from unittest import makeSuite
from unittest import TestCase
from unittest import TestSuite
from persistent.mapping import PersistentMapping
from zope.interface.verify import verifyClass
from plone.keyring.interfaces import IKeyManager
from plone.keyring.keymanager import KeyManager


marker=[]

class MockRing:
    rotated=False
    cleared=False
    def clear(self):
        self.cleared=True
    def rotate(self):
        self.rotated=True



class KeyManagerTests(TestCase):
    def setUp(self):
        self.mgr=KeyManager()
        del self.mgr[u"_system"]
        self.mgr[u"_system"]=MockRing()
        self.mgr[u"one"]=MockRing()
        self.mgr[u"two"]=MockRing()


    def testInterface(self):
        verifyClass(IKeyManager, KeyManager)


    def testSystemKeyringCreated(self):
        mgr=KeyManager()
        self.assertEqual(mgr.keys(), [ u"_system" ])
        self.failUnless(mgr[u"_system"].current is not None)


    def testContainerIsPersistent(self):
        mgr=KeyManager()
        self.failUnless(isinstance(mgr.__dict__["_SampleContainer__data"],
                                   PersistentMapping))


    def testClear(self):
        self.mgr.clear()
        self.assertEqual(self.mgr[u"_system"].cleared, True)
        self.assertEqual(self.mgr[u"one"].cleared, False)
        self.assertEqual(self.mgr[u"two"].cleared, False)


    def testClearGivenRing(self):
        self.mgr.clear(u"one")
        self.assertEqual(self.mgr[u"_system"].cleared, False)
        self.assertEqual(self.mgr[u"one"].cleared, True)
        self.assertEqual(self.mgr[u"two"].cleared, False)


    def testClearAll(self):
        self.mgr.clear(None)
        self.assertEqual(self.mgr[u"_system"].cleared, True)
        self.assertEqual(self.mgr[u"one"].cleared, True)
        self.assertEqual(self.mgr[u"two"].cleared, True)


    def testClearUnknownRing(self):
        self.assertRaises(KeyError, self.mgr.clear, u"missing")


    def testRotate(self):
        self.mgr.rotate()
        self.assertEqual(self.mgr[u"_system"].rotated, True)
        self.assertEqual(self.mgr[u"one"].rotated, False)
        self.assertEqual(self.mgr[u"two"].rotated, False)


    def testRotateGivenRing(self):
        self.mgr.rotate(u"one")
        self.assertEqual(self.mgr[u"_system"].rotated, False)
        self.assertEqual(self.mgr[u"one"].rotated, True)
        self.assertEqual(self.mgr[u"two"].rotated, False)


    def testRotateAll(self):
        self.mgr.rotate(None)
        self.assertEqual(self.mgr[u"_system"].rotated, True)
        self.assertEqual(self.mgr[u"one"].rotated, True)
        self.assertEqual(self.mgr[u"two"].rotated, True)


    def testRotateUnknownRing(self):
        self.assertRaises(KeyError, self.mgr.clear, u"missing")


    def testSecret(self):
        self.mgr[u"_system"].secret=marker
        self.failUnless(self.mgr.secret() is marker)

    def testSecretGivenRing(self):
        self.mgr[u"one"].secret=marker
        self.failUnless(self.mgr.secret(u"one") is marker)

    def testSecretUnknownRing(self):
        self.assertRaises(KeyError, self.mgr.secret, u"missing")

def test_suite():
    suite=TestSuite()
    suite.addTest(makeSuite(KeyManagerTests))
    return suite

