__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

import bitcodin
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetApiBaseTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetApiBaseTestCase, self).setUp()

    def runTest(self):
        api_base = bitcodin.api_base
        api_base_got = bitcodin.get_api_base()
        self.assertEqual(api_base, api_base_got)

    def tearDown(self):
        super(GetApiBaseTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
