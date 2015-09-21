__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_input
from bitcodin import delete_input
from bitcodin import Input
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateInputTestCase, self).setUp()
        self.inputUrl = 'http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv'

    def runTest(self):
        input = Input(self.inputUrl)
        self.input = create_input(input)
        self.assertEquals(self.input.url, input.url)

    def tearDown(self):
        delete_input(self.input.input_id)
        super(CreateInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
