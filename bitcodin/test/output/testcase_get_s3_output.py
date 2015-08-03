__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin import get_output
from bitcodin import S3Output
from bitcodin.test.settings import aws_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetS3OutputTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetS3OutputTestCase, self).setUp()
        self.s3_configuration = {
            'name': 'Python API Test Output',
            'host': aws_config.get('host', None),
            'access_key': aws_config.get('access_key', None),
            'secret_key': aws_config.get('secret_key', None),
            'bucket': aws_config.get('bucket', None),
            'prefix': aws_config.get('prefix', None),
            'region': aws_config.get('region', None),
            'make_public': False
        }
        output = S3Output(
            access_key=self.s3_configuration.get('access_key'),
            secret_key=self.s3_configuration.get('secret_key'),
            name=self.s3_configuration.get('name'),
            host=self.s3_configuration.get('host'),
            bucket=self.s3_configuration.get('bucket'),
            prefix=self.s3_configuration.get('prefix'),
            region=self.s3_configuration.get('region'),
            make_public=self.s3_configuration.get('make_public')
        )
        self.output = create_output(output)


    def runTest(self):
        output = get_output(self.output.output_id)

        self.assertEquals(self.output.name, output.name)
        self.assertEquals(self.output.bucket, output.bucket)
        self.assertEquals(self.output.prefix, output.prefix)
        self.assertEquals(self.output.region, output.region)
        self.assertEquals(self.output.make_public, output.make_public)


    def tearDown(self):
        delete_output(self.output.output_id)
        super(GetS3OutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
