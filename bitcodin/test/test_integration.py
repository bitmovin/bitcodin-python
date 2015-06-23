__author__ = 'dmoser'

import unittest
import bitcodin

bitcodin.api_key = 'yoursuperfancyencryptedapikeyF'


class TestInput(unittest.TestCase):

    def test_create_input(self):

        input_obj = bitcodin.Input(url='http://www.example.com/yourfolder/yourmovie.mp4')
        input_response = bitcodin.create_input(input_obj)

        self.assertEqual(input_response.url, 'http://www.example.com/yourfolder/yourmovie.mp4')
        self.assertEqual(input_response.filename, 'yourmovie.mp4')
        self.assertEqual(input_response.input_type, 'url')

    def test_get_input(self):

        input_response = bitcodin.get_input(3)
        self.assertEqual(input_response.input_id, 2)


class TestEncodingProfile(unittest.TestCase):

    def test_create_encoding_profile(self):

        video_configs = list()
        video_config1 = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
                                                   preset='standard', height=1024, width=768)
        video_config2 = bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
                                                   preset='standard', height=480, width=320)
        video_configs.append(video_config1)
        video_configs.append(video_config2)

        audio_configs = list()
        audio_config = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)
        audio_configs.append(audio_config)

        encoding_profile = bitcodin.create_encoding_profile('API Test Profile', video_configs, audio_configs)

        self.assertEqual(encoding_profile.video_stream_configs[0].profile, 'Main')
        self.assertEqual(encoding_profile.name, 'bitcodin Encoding Profile')
        self.assertEqual(encoding_profile.encoding_profile_id, 5)
        self.assertEqual(encoding_profile.type, 'private')

        self.assertEqual(encoding_profile.audio_stream_configs[0].sample_rate, 48000)

    def test_get_encoding_profile(self):

        encoding_profile = bitcodin.get_encoding_profile(1)
        self.assertEqual(encoding_profile.name, 'Default Release Settings')


class TestJob(unittest.TestCase):

    def test_create_job(self):

        input_obj = bitcodin.Input(url='http://www.example.com/yourfolder/yourmovie.mp4')
        input_obj = bitcodin.create_input(input_obj)

        video_configs = list()
        video_config1 = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
                                                   preset='standard', height=1024, width=768)
        video_config2 = bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
                                                   preset='standard', height=480, width=320)
        video_configs.append(video_config1)
        video_configs.append(video_config2)

        audio_configs = list()
        audio_config = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)
        audio_configs.append(audio_config)

        encoding_profile = bitcodin.create_encoding_profile('API Test Profile', video_configs, audio_configs)

        manifests = ['mpd', 'm3u8']
        job = bitcodin.create_job(input_obj.input_id, encoding_profile.encoding_profile_id, manifests)
        self.assertEqual(job.status, 'Enqueued')

    def test_get_job(self):

        job = bitcodin.get_job(3)
        self.assertEqual(job.status, 'Finished')

if __name__ == '__main__':
    unittest.main()
