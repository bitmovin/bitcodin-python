__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

import bitcodin
from bitcodin.test.bitcodin_test_case import BitcodinTestCase
from bitcodin.exceptions import BitcodinUnknownApiRequestUrlError
from bitcodin.rest import RestClient


class ApiKeyAuthorizedTestCase(BitcodinTestCase):
    def setUp(self):
        super(ApiKeyAuthorizedTestCase, self).setUp()

    def runTest(self):
        with self.assertRaises(BitcodinUnknownApiRequestUrlError):
            response = RestClient.get(url=bitcodin.get_api_base(), headers=bitcodin.create_headers())

    def tearDown(self):
        super(ApiKeyAuthorizedTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
