__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

import bitcodin
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateHttpHeadersTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateHttpHeadersTestCase, self).setUp()

    def runTest(self):
        expected_headers = {
            'Content-Type': 'application/json',
            'bitcodin-api-key': bitcodin.api_key
        }
        headers = bitcodin.create_headers()
        self.assertDictEqual(expected_headers, headers)

    def tearDown(self):
        super(CreateHttpHeadersTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
