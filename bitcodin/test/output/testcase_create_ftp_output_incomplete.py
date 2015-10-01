__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_output
from bitcodin import FTPOutput
from bitcodin.test.settings import ftp_output_config
from bitcodin.exceptions import BitcodinBadRequestError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateFTPOutputIncompleteDataTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateFTPOutputIncompleteDataTestCase, self).setUp()
        self.ftp_configuration = {
            'name': 'Python API Test FTP Output',
            'host': ftp_output_config.get('host', None),
            'username': ftp_output_config.get('username', None),
            'password': ftp_output_config.get('password', None),
            'passive': True
        }

    def runTest(self):
        output = FTPOutput(
            name=self.ftp_configuration.get('name'),
            host='',
            basic_auth_user=self.ftp_configuration.get('username'),
            basic_auth_password=self.ftp_configuration.get('password'),
            passive=self.ftp_configuration.get('passive')
        )

        with self.assertRaises(BitcodinBadRequestError):
            result = create_output(output)

    def tearDown(self):
        super(CreateFTPOutputIncompleteDataTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
