__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

# TODO!

import unittest
from bitcodin import create_job
from bitcodin import create_input
from bitcodin import create_encoding_profile
from bitcodin import delete_input
from bitcodin import delete_encoding_profile
from bitcodin import get_job_status
from bitcodin import Job
from bitcodin import Input
from bitcodin import AudioStreamConfig
from bitcodin import VideoStreamConfig
from bitcodin import EncodingProfile
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetJobStatusTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetJobStatusTestCase, self).setUp()
        self.maxDiff = None

        inputUrl = 'http://eu-storage.bitcodin.com/inputs/Sintel.2010.720p.mkv'
        input = Input(inputUrl)
        self.input = create_input(input)
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=0, bitrate=512000,
            profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        self.manifests = ['m3u8', 'mpd']
        job = Job(self.input.input_id, self.encoding_profile.encoding_profile_id, self.manifests)
        self.job = create_job(job)


    def runTest(self):
        job_status = get_job_status(self.job.job_id)
        self.assertEquals(job_status.job_id, self.job.job_id)
        self.assertEquals(job_status.status, 'Enqueued')


    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(GetJobStatusTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
