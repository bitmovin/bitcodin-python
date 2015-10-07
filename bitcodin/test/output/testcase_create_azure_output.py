__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin import AzureOutput
from bitcodin.test.settings import azure_output_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateAzureOutputTestCase(BitcodinTestCase):

    output = None

    def setUp(self):
        super(CreateAzureOutputTestCase, self).setUp()

    def runTest(self):
        output = AzureOutput(
            name='Azure Test Output Python',
            account_name=azure_output_config.get('accountName'),
            account_key=azure_output_config.get('accountKey'),
            container=azure_output_config.get('container'),
            prefix=azure_output_config.get('prefix')
        )

        self.output = create_output(output)
        self.assertEquals(self.output.name, output.name)
        self.assertEquals(self.output.container, output.container)

    def tearDown(self):
        delete_output(self.output.output_id)
        super(CreateAzureOutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
