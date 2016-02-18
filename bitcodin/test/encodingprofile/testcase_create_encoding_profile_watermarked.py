__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import EncodingProfile
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import create_encoding_profile
from bitcodin import delete_encoding_profile
from bitcodin import WatermarkConfig
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateEncodingProfileWithWatermarkTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateEncodingProfileWithWatermarkTestCase, self).setUp()

    def runTest(self):
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=1, bitrate=512000,
                                                profile='Main', preset='premium', height=480, width=640)

        watermark_config = WatermarkConfig(
            image_url='http://bitdash-a.akamaihd.net/webpages/bitcodin/images/bitcodin-bitmovin-logo-small.png',
            bottom=200,
            right=100
        )

        encoding_profile = EncodingProfile(
            name='API Test Profile',
            video_stream_configs=[video_stream_config],
            audio_stream_configs=[audio_stream_config],
            watermark_config=watermark_config
        )

        result = create_encoding_profile(encoding_profile)
        self.encoding_profile = result
        self.assertEquals(result.name, 'API Test Profile')
        self.assertEquals(result.video_stream_configs[0].default_stream_id, 1)
        self.assertEquals(result.video_stream_configs[0].bitrate, 512000)
        self.assertEquals(result.video_stream_configs[0].profile, 'Main')
        self.assertEquals(result.video_stream_configs[0].preset.lower(), 'standard')
        self.assertEquals(result.video_stream_configs[0].height, 480)
        self.assertEquals(result.video_stream_configs[0].width, 640)
        self.assertEquals(result.audio_stream_configs[0].default_stream_id, 0)
        self.assertEquals(result.audio_stream_configs[0].bitrate, 192000)
        self.assertEquals(result.watermark_config.image,
                          'http://bitdash-a.akamaihd.net/webpages/bitcodin/images/bitcodin-bitmovin-logo-small.png')
        self.assertEquals(result.watermark_config.bottom, 200)
        self.assertEquals(result.watermark_config.right, 100)

    def tearDown(self):
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateEncodingProfileWithWatermarkTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
