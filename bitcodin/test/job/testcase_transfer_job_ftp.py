__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from time import sleep, time
from bitcodin import create_job
from bitcodin import create_input
from bitcodin import create_encoding_profile
from bitcodin import delete_input
from bitcodin import delete_encoding_profile
from bitcodin import transfer_job
from bitcodin import create_output
from bitcodin import delete_output
from bitcodin import get_job_status
from bitcodin import Job
from bitcodin import Input
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin import FTPOutput
from bitcodin.exceptions import BitcodinError
from bitcodin.test.settings import ftp_output_config
from bitcodin.test.config import test_video_url
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class TransferJobToFTPTestCase(BitcodinTestCase):
    def setUp(self):
        super(TransferJobToFTPTestCase, self).setUp()
        self.maxDiff = None

        input_url = test_video_url
        input = Input(input_url)
        self.input = create_input(input)
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=0, bitrate=512000,
                                                profile='Main', preset='premium', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        self.manifests = ['m3u8', 'mpd']
        job = Job(
            input_id=self.input.input_id,
            encoding_profile_id=self.encoding_profile.encoding_profile_id,
            manifest_types=self.manifests
        )
        self.job = create_job(job)
        self.ftp_configuration = {
            'name': 'Python API Test FTP Output',
            'host': ftp_output_config.get('host', None),
            'username': ftp_output_config.get('username', None),
            'password': ftp_output_config.get('password', None),
            'passive': True
        }
        output = FTPOutput(
            name=self.ftp_configuration.get('name'),
            host=self.ftp_configuration.get('host'),
            basic_auth_user=self.ftp_configuration.get('username'),
            basic_auth_password=self.ftp_configuration.get('password'),
            passive=self.ftp_configuration.get('passive')
        )
        self.output = create_output(output)

    def runTest(self):
        start_time = time()
        time_limit = 1200
        while(True):
            job_status = get_job_status(self.job.job_id)
            if(job_status.status.lower() == 'finished'):
                break
            elif(job_status.status.lower() == 'error'):
                raise BitcodinError('An error occured while waiting for job to be FINISHED', 'Job status changed to ERROR!')
            elif(time() - start_time > time_limit):
                raise BitcodinError('Timeout of job duration exceeded!', 'Job took too long!')
            sleep(2)
        transfer = transfer_job(self.job.job_id, self.output.output_id)

    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        delete_output(self.output.output_id)
        super(TransferJobToFTPTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
