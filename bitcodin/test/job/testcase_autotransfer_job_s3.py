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
from bitcodin import S3Output
from bitcodin.exceptions import BitcodinError
from bitcodin.test.settings import s3_output_config
from bitcodin.test.config import test_video_url
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class AutoTransferJobToS3TestCase(BitcodinTestCase):
    def setUp(self):
        super(AutoTransferJobToS3TestCase, self).setUp()
        self.maxDiff = None

        input_url = test_video_url
        input = Input(input_url)
        self.input = create_input(input)
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=0, bitrate=512000,
                                                profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        self.manifests = ['m3u8', 'mpd']
        self.s3_configuration = {
            'name': 'Python API Test Output',
            'host': s3_output_config.get('host', None),
            'access_key': s3_output_config.get('access_key', None),
            'secret_key': s3_output_config.get('secret_key', None),
            'bucket': s3_output_config.get('bucket', None),
            'prefix': s3_output_config.get('prefix', None),
            'region': s3_output_config.get('region', None),
            'make_public': False
        }
        output = S3Output(
            name=self.s3_configuration.get('name'),
            host=self.s3_configuration.get('host'),
            access_key=self.s3_configuration.get('access_key'),
            secret_key=self.s3_configuration.get('secret_key'),
            bucket=self.s3_configuration.get('bucket'),
            prefix=self.s3_configuration.get('prefix'),
            region=self.s3_configuration.get('region'),
            make_public=self.s3_configuration.get('make_public')
        )
        self.output = create_output(output)

    def runTest(self):
        job = Job(
            input_id=self.input.input_id,
            encoding_profile_id=self.encoding_profile.encoding_profile_id,
            manifest_types=self.manifests,
            output_id=self.output.output_id
        )
        self.job = create_job(job)
        self.wait_until_job_finished(self.job.id)

    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(AutoTransferJobToS3TestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
