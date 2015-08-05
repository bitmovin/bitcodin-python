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
from bitcodin import PlayreadyWidevineCombinedDrmConfig
from bitcodin.exceptions import BitcodinBadRequestError
from bitcodin.test.config import test_video_url
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateJobPlayreadyWidevineDrmInvalidConfigTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateJobPlayreadyWidevineDrmInvalidConfigTestCase, self).setUp()
        inputUrl = test_video_url
        input = Input(inputUrl)
        self.input = create_input(input)
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=0, bitrate=512000,
            profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        self.manifests = ['m3u8', 'mpd']
        # TODO write playready_widevine drm_config (invalid)
        self.drm_config = PlayreadyWidevineCombinedDrmConfig(
            key=None,
            pssh=None,
            kid=None,
            la_url=None,
            lui_url=None,
            ds_id=None,
            custom_attributes=None,
            method=None
        )


    def runTest(self):
        job = Job(self.input.input_id, self.encoding_profile.encoding_profile_id, self.manifests, 'standard', self.drm_config)
        with self.assertRaises(BitcodinBadRequestError):
            self.job = create_job(job)


    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateJobPlayreadyWidevineDrmInvalidConfigTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
