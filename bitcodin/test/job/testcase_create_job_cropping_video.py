__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_job
from bitcodin import create_input
from bitcodin import create_encoding_profile
from bitcodin import delete_input
from bitcodin import delete_encoding_profile
from bitcodin import Job
from bitcodin import Input
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin import CroppingConfig
from bitcodin.test.config import test_video_url
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateJobWithVideoCroppingTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateJobWithVideoCroppingTestCase, self).setUp()
        input_url = test_video_url
        input = Input(input_url)
        self.input = create_input(input)
        audio_stream_config = AudioStreamConfig(
            default_stream_id=0,
            bitrate=192000
        )
        video_stream_config = VideoStreamConfig(
            default_stream_id=0,
            bitrate=512000,
            profile='Main',
            preset='standard',
            height=480,
            width=640
        )
        cropping_config = CroppingConfig(
            top=100,
            bottom=100,
            left=5,
            right=50
        )

        encoding_profile = EncodingProfile(
            name='API Test Profile',
            video_stream_configs=[video_stream_config],
            audio_stream_configs=[audio_stream_config],
            cropping_config=cropping_config
        )
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
        self.assertEquals(self.job.input.url, self.input.url)
        self.assertEquals(self.job.encoding_profiles[0].encoding_profile_id, job.encodingProfileId)
        self.assertEquals(self.encoding_profile.cropping_config.top, 100)
        self.assertEquals(self.encoding_profile.cropping_config.bottom, 100)
        self.assertEquals(self.encoding_profile.cropping_config.left, 5)
        self.assertEquals(self.encoding_profile.cropping_config.right, 50)

    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateJobWithVideoCroppingTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
