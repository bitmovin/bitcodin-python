__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_input
from bitcodin import delete_input
from bitcodin import Input
from bitcodin import list_inputs
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetInputListTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetInputListTestCase, self).setUp()
        input_url = 'http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv'
        input = Input(input_url)
        self.input = create_input(input)

    def runTest(self):
        inputs = list_inputs()
        input_found = False
        for input in inputs:
            if self.input.input_id == input.input_id:
                input_found = True
                break
        self.assertEquals(input_found, True)

    def tearDown(self):
        delete_input(self.input.input_id)
        super(GetInputListTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
