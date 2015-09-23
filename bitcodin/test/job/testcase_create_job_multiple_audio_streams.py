__author__ = 'Guenther Cwioro <guenther.cwioro@bitmovin.net>'

import unittest
from bitcodin import create_job, AudioMetaData
from bitcodin import create_input
from bitcodin import create_encoding_profile
from bitcodin import delete_input
from bitcodin import delete_encoding_profile
from bitcodin import Job
from bitcodin import Input
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin import DrmConfig
from bitcodin import WidevineDrmConfig
from bitcodin import PlayreadyDrmConfig
from bitcodin.exceptions import BitcodinBadRequestError
from bitcodin.test.config import test_video_url_multiple_audio_streams
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class CreateJobWithMultipleAudioStreamsTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateJobWithMultipleAudioStreamsTestCase, self).setUp()
        inputUrl = test_video_url_multiple_audio_streams
        input = Input(inputUrl)
        self.input = create_input(input)
        audio_stream_config_0 = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        audio_stream_config_1 = AudioStreamConfig(default_stream_id=1, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=0, bitrate=512000,
            profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config_0, audio_stream_config_1])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        self.manifests = ['m3u8', 'mpd']
        self.audio_meta_data = {}

        audio_stream_config_0_meta_data = AudioMetaData(0,  'de', 'Just Sound')
        audio_stream_config_1_meta_data = AudioMetaData(1,  'en', 'Sound and Voice')

        self.audio_meta_data = [audio_stream_config_0_meta_data, audio_stream_config_1_meta_data]

    def runTest(self):
        job = Job(
            input_id=self.input.input_id,
            encoding_profile_id=self.encoding_profile.encoding_profile_id,
            manifest_types=self.manifests,
            speed='standard',
            audio_meta_data=self.audio_meta_data
        )
        self.job = create_job(job)
        self.assertEquals(self.job.input.input_id, job.inputId)
        self.assertEquals(self.job.input.url, self.input.url)
        self.assertEquals(self.job.encoding_profiles[0].encoding_profile_id, job.encodingProfileId)

    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateJobWithMultipleAudioStreamsTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
