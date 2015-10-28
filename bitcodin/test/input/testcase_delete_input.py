__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import Input
from bitcodin import create_input
from bitcodin import delete_input
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class DeleteInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(DeleteInputTestCase, self).setUp()
        input_url = 'http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv'
        input = Input(input_url)
        self.input = create_input(input)

    def runTest(self):
        delete_input(self.input.input_id)

    def tearDown(self):
        super(DeleteInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
