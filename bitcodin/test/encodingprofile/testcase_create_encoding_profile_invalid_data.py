__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin import create_encoding_profile
from bitcodin.exceptions import BitcodinBadRequestError
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateEncodingProfileInvalidDataTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateEncodingProfileInvalidDataTestCase, self).setUp()

    def runTest(self):
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=1, bitrate=512000,
                                                profile='Mainerr', preset='nonexpreset', height=480, width=640)

        encoding_profile = EncodingProfile('API Test Profile X', [video_stream_config], [audio_stream_config])
        with self.assertRaises(BitcodinBadRequestError):
            result = create_encoding_profile(encoding_profile)

    def tearDown(self):
        super(CreateEncodingProfileInvalidDataTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
