__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin import FTPOutput
from bitcodin.test.settings import ftp_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase

class CreateFTPOutputTestCase(BitcodinTestCase):

    output = None
    def setUp(self):
        super(CreateFTPOutputTestCase, self).setUp()
        self.ftp_configuration = {
            'name': 'Python API Test FTP Output',
            'host': ftp_config.get('host', None),
            'username': ftp_config.get('username', None),
            'password': ftp_config.get('password', None),
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
        self.assertEquals(self.output.name, output.name)
        self.assertEquals(self.output.host, output.host.split('/')[0])
        self.assertEquals(self.output.passive, output.passive)

    def tearDown(self):
        delete_output(self.output.output_id)
        super(CreateFTPOutputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
