__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin import get_output
from bitcodin import GCSOutput
from bitcodin.test.settings import gcs_output_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetGCSOutputTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetGCSOutputTestCase, self).setUp()
        output = GCSOutput(
            name='Python Test Output',
            access_key=gcs_output_config.get('accessKey'),
            secret_key=gcs_output_config.get('secretKey'),
            bucket=gcs_output_config.get('bucket'),
            prefix=gcs_output_config.get('prefix'),
            make_public=False
        )
        self.output = create_output(output)
        self.output = get_output(self.output.output_id)

    def runTest(self):
        output = get_output(self.output.output_id)
        self.assertEquals(self.output.name, output.name)
        self.assertEquals(self.output.bucket, output.bucket)
        self.assertEquals(self.output.prefix, output.prefix)

    def tearDown(self):
        delete_output(self.output.output_id)
        super(GetGCSOutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
