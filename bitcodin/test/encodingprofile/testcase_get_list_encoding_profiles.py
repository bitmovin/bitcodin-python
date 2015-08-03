__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin import create_encoding_profile
from bitcodin import list_encoding_profiles
from bitcodin import delete_encoding_profile
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetEncodingProfileListTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetEncodingProfileListTestCase, self).setUp()
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=1, bitrate=512000,
            profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)

    def runTest(self):
        encoding_profiles = list_encoding_profiles()
        encoding_profile_found = False
        for encoding_profile in encoding_profiles:
            if self.encoding_profile.encoding_profile_id == encoding_profile.encoding_profile_id:
                encoding_profile_found = True
                break
        self.assertEquals(encoding_profile_found, True)

    def tearDown(self):
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(GetEncodingProfileListTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
