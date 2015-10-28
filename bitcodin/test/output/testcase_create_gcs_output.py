__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin import GCSOutput
from bitcodin.test.settings import gcs_output_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase

class CreateGCSOutputTestCase(BitcodinTestCase):

    output = None
    def setUp(self):
        super(CreateGCSOutputTestCase, self).setUp()

    def runTest(self):
        output = GCSOutput(
            name='Python Test Output',
            access_key=gcs_output_config.get('accessKey'),
            secret_key=gcs_output_config.get('secretKey'),
            bucket=gcs_output_config.get('bucket'),
            prefix=gcs_output_config.get('prefix'),
            make_public=False
        )

        self.output = create_output(output)
        self.assertEquals(self.output.name, output.name)
        self.assertEquals(self.output.bucket, output.bucket)

    def tearDown(self):
        delete_output(self.output.output_id)
        super(CreateGCSOutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
