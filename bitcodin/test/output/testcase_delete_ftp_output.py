__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import FTPOutput
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin import get_output
from bitcodin.exceptions import BitcodinNotFoundError
from bitcodin.test.settings import ftp_output_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class DeleteFTPOutputTestCase(BitcodinTestCase):
    def setUp(self):
        super(DeleteFTPOutputTestCase, self).setUp()
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
            host=self.ftp_configuration.get('host'),
            basic_auth_user=self.ftp_configuration.get('username'),
            basic_auth_password=self.ftp_configuration.get('password'),
            passive=self.ftp_configuration.get('passive')
        )
        self.output = create_output(output)
        self.assertIsNotNone(self.output.output_id)

        delete_output(self.output.output_id)
        with self.assertRaises(BitcodinNotFoundError):
            get_output(self.output.output_id)

    def tearDown(self):
        super(DeleteFTPOutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
