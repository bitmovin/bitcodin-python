__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import EncodingProfile
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import create_encoding_profile
from bitcodin import delete_encoding_profile
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateEncodingProfileTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateEncodingProfileTestCase, self).setUp()

    def runTest(self):
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=1, bitrate=512000,
            profile='Main', preset='premium', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        result = create_encoding_profile(encoding_profile)
        self.encoding_profile = result
        self.assertEquals(result.name, 'API Test Profile')
        self.assertEquals(result.video_stream_configs[0].default_stream_id, 1)
        self.assertEquals(result.video_stream_configs[0].bitrate, 512000)
        self.assertEquals(result.video_stream_configs[0].profile, 'Main')
        self.assertEquals(result.video_stream_configs[0].preset.lower(), 'premium')
        self.assertEquals(result.video_stream_configs[0].height, 480)
        self.assertEquals(result.video_stream_configs[0].width, 640)
        self.assertEquals(result.audio_stream_configs[0].default_stream_id, 0)
        self.assertEquals(result.audio_stream_configs[0].bitrate, 192000)

    def tearDown(self):
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateEncodingProfileTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
