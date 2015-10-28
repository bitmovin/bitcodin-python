#!/usr/bin/env python

import unittest
from bitcodin.test.bitcodin_test_case import BitcodinTestCase

import bitcodin
import time
from bitcodin import EncodingProfile
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import create_encoding_profile
from bitcodin import GCSOutput
from bitcodin.test.settings import gcs_output_config


class CreateLiveStreamTestCase(BitcodinTestCase):

    def setUp(self):
        output = GCSOutput(
            name='Python Live GCS Output',
            access_key=gcs_output_config.get('accessKey'),
            secret_key=gcs_output_config.get('secretKey'),
            bucket=gcs_output_config.get('bucket'),
            prefix=gcs_output_config.get('prefix'),
            make_public=False
        )
        self.output = bitcodin.create_output(output)

        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=1, bitrate=512000,
                                                profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Live Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        super(CreateLiveStreamTestCase, self).setUp()

    def runTest(self):
        self.assertIsNotNone(self.encoding_profile.encoding_profile_id)
        self.assertIsNotNone(self.output.output_id)

        live_stream = bitcodin.LiveStream("test-live-stream",
                                          "stream",
                                          self.encoding_profile.encoding_profile_id,
                                          120,
                                          self.output.output_id)

        live_stream = bitcodin.create_live_instance(live_stream)

        self.assertIsNotNone(live_stream.id)
        self.assertEqual(live_stream.status, 'STARTING')
        self.assertEqual(live_stream.stream_key, "stream")

        while live_stream.status != 'RUNNING' and live_stream.status != 'ERROR':
            live_stream = bitcodin.get_live_instance(live_stream.id)
            time.sleep(2)

        self.assertEqual(live_stream.status, 'RUNNING')
        self.assertIsNotNone(live_stream.created_at)

        bitcodin.delete_live_instance(live_stream.id)

        while live_stream.status != 'TERMINATED' and live_stream.status != 'ERROR':
            live_stream = bitcodin.get_live_instance(live_stream.id)
            time.sleep(2)

        self.assertEqual(live_stream.status, 'TERMINATED')
        self.assertIsNotNone(live_stream.terminated_at)


if __name__ == '__main__':
    unittest.main()
