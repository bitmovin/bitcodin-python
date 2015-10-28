__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import GCSOutput
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin.test.settings import gcs_output_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class DeleteGCSOutputTestCase(BitcodinTestCase):
    def setUp(self):
        super(DeleteGCSOutputTestCase, self).setUp()
        output = GCSOutput(
            name='Python Test Output',
            access_key=gcs_output_config.get('accessKey'),
            secret_key=gcs_output_config.get('secretKey'),
            bucket=gcs_output_config.get('bucket'),
            prefix=gcs_output_config.get('prefix'),
            make_public=False
        )
        self.output = create_output(output)

    def runTest(self):
        delete_output(self.output.output_id)

    def tearDown(self):
        super(DeleteGCSOutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
