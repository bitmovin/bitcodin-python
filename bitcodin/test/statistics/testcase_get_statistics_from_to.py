__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

import bitcodin
from bitcodin.test.bitcodin_test_case import BitcodinTestCase
from bitcodin.rest import RestClient


class GetStatisticsFromToTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetStatisticsFromToTestCase, self).setUp()

    def runTest(self):
        response = RestClient.get(url=bitcodin.get_api_base()+'/statistics/2000-12-24/2100-12-24', headers=bitcodin.create_headers())

    def tearDown(self):
        super(GetStatisticsFromToTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
