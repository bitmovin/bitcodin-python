__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

import bitcodin
from bitcodin.test.bitcodin_test_case import BitcodinTestCase
from bitcodin.rest import RestClient


class GetStatisticsCurrentMonthTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetStatisticsCurrentMonthTestCase, self).setUp()

    def runTest(self):
        response = RestClient.get(url=bitcodin.get_api_base()+'/statistics', headers=bitcodin.create_headers())

    def tearDown(self):
        super(GetStatisticsCurrentMonthTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
