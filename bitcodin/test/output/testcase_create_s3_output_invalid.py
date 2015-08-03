__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_output
from bitcodin import S3Output
from bitcodin.test.settings import aws_config
from bitcodin.exceptions import BitcodinBadRequestError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateS3OutputInvalidDataTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateS3OutputInvalidDataTestCase, self).setUp()
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

    def runTest(self):
        output = S3Output(
            name=self.s3_configuration.get('name'),
            host=self.s3_configuration.get('host'),
            access_key=self.s3_configuration.get('access_key'),
            secret_key=self.s3_configuration.get('secret_key'),
            bucket=self.s3_configuration.get('bucket'),
            prefix=self.s3_configuration.get('prefix'),
            region='eu-south-22',
            make_public=self.s3_configuration.get('make_public')
        )

        with self.assertRaises(BitcodinBadRequestError):
            result = create_output(output)

    def tearDown(self):
        super(CreateS3OutputInvalidDataTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
