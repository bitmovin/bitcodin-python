__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import delete_input
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class DeleteNonExistentInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(DeleteNonExistentInputTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinNotFoundError):
            delete_input(0)

    def tearDown(self):
        super(DeleteNonExistentInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
