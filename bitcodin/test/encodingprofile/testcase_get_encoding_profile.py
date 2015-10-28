__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import get_encoding_profile
from bitcodin import EncodingProfile
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import create_encoding_profile
from bitcodin import delete_encoding_profile
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetEncodingProfileTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetEncodingProfileTestCase, self).setUp()
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=1, bitrate=512000,
            profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.created_encoding_profile = create_encoding_profile(encoding_profile)

    def runTest(self):
        id = self.created_encoding_profile.encoding_profile_id
        encoding_profile = get_encoding_profile(id)
        self.assertEquals(self.created_encoding_profile.encoding_profile_id, encoding_profile.encoding_profile_id)
        self.assertEquals(self.created_encoding_profile.name, encoding_profile.name)
        self.assertEquals(self.created_encoding_profile.video_stream_configs[0].default_stream_id, encoding_profile.video_stream_configs[0].default_stream_id)
        self.assertEquals(self.created_encoding_profile.video_stream_configs[0].bitrate, encoding_profile.video_stream_configs[0].bitrate)
        self.assertEquals(self.created_encoding_profile.video_stream_configs[0].profile, encoding_profile.video_stream_configs[0].profile)
        self.assertEquals(self.created_encoding_profile.video_stream_configs[0].preset.lower(), encoding_profile.video_stream_configs[0].preset.lower())
        self.assertEquals(self.created_encoding_profile.video_stream_configs[0].height, encoding_profile.video_stream_configs[0].height)
        self.assertEquals(self.created_encoding_profile.video_stream_configs[0].width, encoding_profile.video_stream_configs[0].width)
        self.assertEquals(self.created_encoding_profile.audio_stream_configs[0].default_stream_id, encoding_profile.audio_stream_configs[0].default_stream_id)
        self.assertEquals(self.created_encoding_profile.audio_stream_configs[0].bitrate, encoding_profile.audio_stream_configs[0].bitrate)

    def tearDown(self):
        delete_encoding_profile(self.created_encoding_profile.encoding_profile_id)
        super(GetEncodingProfileTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
