__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import analyze_input
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class AnalyzeNonExistentInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(AnalyzeNonExistentInputTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinNotFoundError):
            encoding_profile = analyze_input(0)

    def tearDown(self):
        super(AnalyzeNonExistentInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
