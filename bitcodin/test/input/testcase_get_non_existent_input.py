__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import get_input
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetNonExistentInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetNonExistentInputTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinNotFoundError):
            encoding_profile = get_input(0)

    def tearDown(self):
        super(GetNonExistentInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
