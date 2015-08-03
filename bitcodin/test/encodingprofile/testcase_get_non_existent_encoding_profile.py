__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import get_encoding_profile
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetNonExistentEncodingProfileTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetNonExistentEncodingProfileTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinNotFoundError):
            encoding_profile = get_encoding_profile(0)

    def tearDown(self):
        super(GetNonExistentEncodingProfileTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
