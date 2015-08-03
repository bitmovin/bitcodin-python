__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import get_api_base
from bitcodin.rest import RestClient
from bitcodin.api import create_headers
from bitcodin.exceptions import BitcodinUnknownApiRequestUrlError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class HttpGetUndefinedTestCase(BitcodinTestCase):
    def setUp(self):
        super(HttpGetUndefinedTestCase, self).setUp()

    def runTest(self):
        headers = create_headers()
        url = get_api_base() + '/MY_SUPER_FANCY_UNDEFINED_URL/'
        with self.assertRaises(BitcodinUnknownApiRequestUrlError):
            response = RestClient.get(url=url, headers=headers)


    def tearDown(self):
        super(HttpGetUndefinedTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
