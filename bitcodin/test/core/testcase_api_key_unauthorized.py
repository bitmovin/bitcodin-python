__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

import bitcodin
from bitcodin.test.bitcodin_test_case import BitcodinTestCase
from bitcodin.exceptions import BitcodinApiKeyNotAuthorizedError
from bitcodin.rest import RestClient


class ApiKeyUnauthorizedTestCase(BitcodinTestCase):
    def setUp(self):
        super(ApiKeyUnauthorizedTestCase, self).setUp()
        bitcodin.api_key = 'A_SUPER_FANCY_INVALID_KEY'

    def runTest(self):
        with self.assertRaises(BitcodinApiKeyNotAuthorizedError):
            response = RestClient.get(url=bitcodin.get_api_base(), headers=bitcodin.create_headers())

    def tearDown(self):
        super(ApiKeyUnauthorizedTestCase, self).tearDown()

if __name__ == '__main__':
    unittest.main()
