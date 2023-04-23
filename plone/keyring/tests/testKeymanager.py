from persistent.mapping import PersistentMapping
from plone.keyring.interfaces import IKeyManager
from plone.keyring.keymanager import KeyManager
from plone.keyring.keyring import Keyring
from unittest import makeSuite
from unittest import TestCase
from unittest import TestSuite
from zope.interface.verify import verifyClass


marker = []


class KeyManagerTests(TestCase):
    def setUp(self):
        self.mgr = KeyManager()
        del self.mgr["_system"]
        self.mgr["_system"] = Keyring()
        self.mgr["_system"].rotate()
        self.mgr["one"] = Keyring()
        self.mgr["one"].rotate()
        self.mgr["two"] = Keyring()
        self.mgr["two"].rotate()

    def testInterface(self):
        verifyClass(IKeyManager, KeyManager)

    def testSystemKeyringCreated(self):
        mgr = KeyManager()
        self.assertEqual(set(mgr), {"_anon", "_forms", "_system"})
        self.assertTrue(mgr["_system"].current is not None)

    def testContainerIsPersistent(self):
        mgr = KeyManager()
        self.assertTrue(
            isinstance(mgr.__dict__["_SampleContainer__data"], PersistentMapping)
        )

    def testClear(self):
        self.mgr.clear()
        self.assertEqual(set(self.mgr["_system"]), {None})
        self.assertNotEqual(set(self.mgr["one"]), {None})
        self.assertNotEqual(set(self.mgr["two"]), {None})

    def testClearGivenRing(self):
        self.mgr.clear("one")
        self.assertNotEqual(set(self.mgr["_system"]), {None})
        self.assertEqual(set(self.mgr["one"]), {None})
        self.assertNotEqual(set(self.mgr["two"]), {None})

    def testClearAll(self):
        self.mgr.clear(None)
        self.assertEqual(set(self.mgr["_system"]), {None})
        self.assertEqual(set(self.mgr["one"]), {None})
        self.assertEqual(set(self.mgr["two"]), {None})

    def testClearUnknownRing(self):
        self.assertRaises(KeyError, self.mgr.clear, "missing")

    def testRotate(self):
        current_sys = self.mgr["_system"].current
        current_one = self.mgr["one"].current
        current_two = self.mgr["two"].current
        self.mgr.rotate()
        self.assertNotEqual(self.mgr["_system"].current, current_sys)
        self.assertEqual(self.mgr["_system"][1], current_sys)
        self.assertEqual(self.mgr["one"].current, current_one)
        self.assertEqual(self.mgr["one"][1], None)
        self.assertEqual(self.mgr["two"].current, current_two)
        self.assertEqual(self.mgr["two"][1], None)

    def testRotateGivenRing(self):
        current_sys = self.mgr["_system"].current
        current_one = self.mgr["one"].current
        current_two = self.mgr["two"].current
        self.mgr.rotate("one")
        self.assertEqual(self.mgr["_system"].current, current_sys)
        self.assertEqual(self.mgr["_system"][1], None)
        self.assertNotEqual(self.mgr["one"].current, current_one)
        self.assertEqual(self.mgr["one"][1], current_one)
        self.assertEqual(self.mgr["two"].current, current_two)
        self.assertEqual(self.mgr["two"][1], None)

    def testRotateAll(self):
        current_sys = self.mgr["_system"].current
        current_one = self.mgr["one"].current
        current_two = self.mgr["two"].current
        self.mgr.rotate(None)
        self.assertNotEqual(self.mgr["_system"].current, current_sys)
        self.assertEqual(self.mgr["_system"][1], current_sys)
        self.assertNotEqual(self.mgr["one"].current, current_one)
        self.assertEqual(self.mgr["one"][1], current_one)
        self.assertNotEqual(self.mgr["two"].current, current_two)
        self.assertEqual(self.mgr["two"][1], current_two)

    def testRotateUnknownRing(self):
        self.assertRaises(KeyError, self.mgr.clear, "missing")

    def testSecret(self):
        self.mgr["_system"][0] = marker
        self.assertTrue(self.mgr.secret() is marker)

    def testSecretGivenRing(self):
        self.mgr["one"][0] = marker
        self.assertTrue(self.mgr.secret("one") is marker)

    def testSecretUnknownRing(self):
        self.assertRaises(KeyError, self.mgr.secret, "missing")


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(KeyManagerTests))
    return suite
