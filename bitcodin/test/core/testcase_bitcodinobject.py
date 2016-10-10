__author__ = 'Jan Češpivo <jan.cespivo@coex.cz>'

import unittest

from bitcodin.resource import BitcodinObject
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class BitcodinObjectBooleanTestCase(BitcodinTestCase):
    def test_not_empty(self):
        not_empty_bitcodin_object = BitcodinObject({'some_key': 'some_value'})
        boolean_representation = bool(not_empty_bitcodin_object)
        self.assertEqual(boolean_representation, True)

    def test_empty(self):
        empty_bitcodin_object = BitcodinObject({})
        boolean_representation = bool(empty_bitcodin_object)
        self.assertEqual(boolean_representation, False)


class BitcodinObjectLengthTestCase(BitcodinTestCase):
    def test_not_empty(self):
        not_empty_bitcodin_object = BitcodinObject({'some_key': 'some_value'})
        length = len(not_empty_bitcodin_object)
        self.assertEqual(length, 1)

    def test_empty(self):
        empty_bitcodin_object = BitcodinObject({})
        length = len(empty_bitcodin_object)
        self.assertEqual(length, 0)


if __name__ == '__main__':
    unittest.main()
