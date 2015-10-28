__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_input
from bitcodin import delete_input
from bitcodin import S3Input
from bitcodin.test.settings import s3_input_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateS3InputTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateS3InputTestCase, self).setUp()

    def runTest(self):
        input = S3Input(
            access_key=s3_input_config.get('access_key'),
            secret_key=s3_input_config.get('secret_key'),
            host=s3_input_config.get('host'),
            bucket=s3_input_config.get('bucket'),
            region=s3_input_config.get('region'),
            object_key=s3_input_config.get('object_key')
        )

        self.input = create_input(input)

        self.assertEquals(self.input.host, input.host)
        self.assertEquals(self.input.bucket, input.bucket)
        self.assertEquals(self.input.region, input.region)
        self.assertEquals(self.input.status, 'CREATED')

    def tearDown(self):
        delete_input(self.input.input_id)
        super(CreateS3InputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
