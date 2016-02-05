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


class CreateJobPlayreadyWidevineDrmTestCase(BitcodinTestCase):
    def setUp(self):
        super(CreateJobPlayreadyWidevineDrmTestCase, self).setUp()
        input_url = test_video_url
        input = Input(input_url)
        self.input = create_input(input)
        audio_stream_config = AudioStreamConfig(default_stream_id=0, bitrate=192000)
        video_stream_config = VideoStreamConfig(default_stream_id=0, bitrate=512000,
                                                profile='Main', preset='standard', height=480, width=640)
        encoding_profile = EncodingProfile('API Test Profile', [video_stream_config], [audio_stream_config])
        self.encoding_profile = create_encoding_profile(encoding_profile)
        self.manifests = ['m3u8', 'mpd']
        self.drm_config = PlayreadyWidevineCombinedDrmConfig(
            key='100b6c20940f779a4589152b57d2dacb',
            pssh='CAESEOtnarvLNF6Wu89hZjDxo9oaDXdpZGV2aW5lX3Rlc3QiEGZrajNsamFTZGZhbGtyM2oqAkhEMgA=',
            kid='eb676abbcb345e96bbcf616630f1a3da',
            la_url='http://playready.directtaps.net/pr/svc/rightsmanager.asmx?PlayRight=1&ContentKey=EAtsIJQPd5pFiRUrV9Layw==',
            lui_url=None,
            ds_id=None,
            custom_attributes=None,
            method='mpeg_cenc'
        )

    def runTest(self):
        job = Job(
            input_id=self.input.input_id,
            encoding_profile_id=self.encoding_profile.encoding_profile_id,
            manifest_types=self.manifests,
            speed='standard',
            drm_config=self.drm_config
        )
        self.job = create_job(job)
        self.assertEquals(self.job.input.input_id, job.inputId)
        self.assertEquals(self.job.input.url, self.input.url)
        self.assertEquals(self.job.encoding_profiles[0].encoding_profile_id, job.encodingProfileId)
        self.wait_until_job_finished(self.job.job_id)


    def tearDown(self):
        delete_input(self.input.input_id)
        delete_encoding_profile(self.encoding_profile.encoding_profile_id)
        super(CreateJobPlayreadyWidevineDrmTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
