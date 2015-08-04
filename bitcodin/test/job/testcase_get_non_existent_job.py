__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import get_job
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetNonExistentJobTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetNonExistentJobTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinNotFoundError):
            get_job(0)

    def tearDown(self):
        super(GetNonExistentJobTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
