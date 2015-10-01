__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_input
from bitcodin import delete_input
from bitcodin import AzureInput
from bitcodin.test.settings import azure_input_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateAzureInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateAzureInputTestCase, self).setUp()

    def runTest(self):
        input = AzureInput(
            account_name=azure_input_config.get('accountName'),
            account_key=azure_input_config.get('accountKey'),
            container=azure_input_config.get('container'),
            url=azure_input_config.get('url')
        )

        self.input = create_input(input)

        self.assertEquals(self.input.filename, input.url)
        self.assertEquals(self.input.status, 'CREATED')

    def tearDown(self):
        delete_input(self.input.input_id)
        super(CreateAzureInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
