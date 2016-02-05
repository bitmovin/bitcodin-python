__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_job
from bitcodin import create_input
from bitcodin import create_encoding_profile
from bitcodin import delete_input
from bitcodin import delete_encoding_profile
from bitcodin import Job
from bitcodin import AzureInput
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin.test.settings import azure_input_config
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateJobAzureInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateJobAzureInputTestCase, self).setUp()

        input = AzureInput(
            account_name=azure_input_config.get('accountName'),
            account_key=azure_input_config.get('accountKey'),
            container=azure_input_config.get('container'),
            url=azure_input_config.get('url')
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
        self.wait_until_job_finished(self.job.job_id)

    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateJobAzureInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
