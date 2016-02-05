__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_job
from bitcodin import create_input
from bitcodin import create_encoding_profile
from bitcodin import delete_input
from bitcodin import delete_encoding_profile
from bitcodin import Job
from bitcodin import S3Input
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin.test.settings import s3_input_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateJobS3InputTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateJobS3InputTestCase, self).setUp()

        input = S3Input(
            access_key=s3_input_config.get('access_key'),
            secret_key=s3_input_config.get('secret_key'),
            host=s3_input_config.get('host'),
            bucket=s3_input_config.get('bucket'),
            region=s3_input_config.get('region'),
            object_key=s3_input_config.get('object_key')
        )

        self.input = create_input(input)
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=0, bitrate=512000,
                                                profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        self.manifests = ['m3u8', 'mpd']

    def runTest(self):
        job = Job(
            input_id=self.input.input_id,
            encoding_profile_id=self.encoding_profile.encoding_profile_id,
            manifest_types=self.manifests,
            speed='standard'
        )
        self.job = create_job(job)
        self.assertEquals(self.job.input.input_id, job.inputId)
        self.assertEquals(self.job.encoding_profiles[0].encoding_profile_id, job.encodingProfileId)
        self.wait_until_job_finished(self.job.id)

    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateJobS3InputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
