__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_input
from bitcodin import Input
from bitcodin.exceptions import BitcodinBadRequestError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateInputInvalidDataTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateInputInvalidDataTestCase, self).setUp()
        self.inputUrl = 'http://myfancyurlwhichdoes.not.exist.com/mydest/mysupervideo.mp4'

    def runTest(self):
        input = Input(self.inputUrl)
        with self.assertRaises(BitcodinBadRequestError):
            result = create_input(input)

    def tearDown(self):
        super(CreateInputInvalidDataTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
