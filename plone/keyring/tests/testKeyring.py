from plone.keyring.interfaces import IKeyring
from plone.keyring.keyring import Keyring
from unittest import defaultTestLoader
from unittest import TestCase
from unittest import TestSuite
from zope.interface.verify import verifyClass

import types


class KeyringTests(TestCase):
    def testInterface(self):
        verifyClass(IKeyring, Keyring)

    def testConstructionDefaultSize(self):
        ring = Keyring()
        self.assertEqual(len(ring), 5)

    def testConstructionSize(self):
        ring = Keyring(3)
        self.assertEqual(len(ring), 3)

    def testKeyringStartsEmpty(self):
        ring = Keyring()
        self.assertEqual(set(list(ring)), {None})

    def testIterate(self):
        ring = Keyring()
        ring.data = [0, 1, 2, 3, 4]
        iterator = ring.__iter__()
        self.assertTrue(isinstance(iterator, types.GeneratorType))
        self.assertEqual(list(iterator), [0, 1, 2, 3, 4])

    def testClear(self):
        ring = Keyring()
        ring.data = [0, 1, 2]
        ring.clear()
        self.assertEqual(ring.data, [None, None, None])

    def testRotate(self):
        ring = Keyring()
        ring.rotate()
        self.assertFalse(ring.current is None)
        self.assertEqual(ring.data[1:], [None, None, None, None])

    def testRotateTwice(self):
        ring = Keyring()
        ring.rotate()
        ring.rotate()
        self.assertTrue(ring.data[0] is not None)
        self.assertTrue(ring.data[1] is not None)
        self.assertEqual(ring.data[2:], [None, None, None])

    def testCurrent(self):
        ring = Keyring()
        marker = []
        ring.data = [marker, 1, 2, 3]
        self.assertTrue(ring.current is marker)


def test_suite():
    suite = TestSuite()
    suite.addTest(defaultTestLoader.loadTestsFromTestCase(KeyringTests))
    return suite
