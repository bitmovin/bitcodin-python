__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import delete_encoding_profile
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class DeleteNonExistentEncodingProfileTestCase(BitcodinTestCase):
    def setUp(self):
        super(DeleteNonExistentEncodingProfileTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinNotFoundError):
            delete_encoding_profile(0)

    def tearDown(self):
        super(DeleteNonExistentEncodingProfileTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
