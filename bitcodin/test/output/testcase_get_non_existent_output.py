__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import get_output
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetNonExistentOutputTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetNonExistentOutputTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinNotFoundError):
            encoding_profile = get_output(0)

    def tearDown(self):
        super(GetNonExistentOutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
