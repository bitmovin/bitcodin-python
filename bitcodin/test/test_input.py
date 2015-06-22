__author__ = 'dmoser'

import unittest
import bitcodin

bitcodin.api_key = 'insertapikeyhere'


class TestInput(unittest.TestCase):

    def test_create_input(self):
        input = bitcodin.create_input(url="http://ftp.nluug.nl/pub/graphics/blender/demo/movies/Sintel.2010.720p.mkv")
        self.assertEqual(input.url, "http://ftp.nluug.nl/pub/graphics/blender/demo/movies/Sintel.2010.720p.mkv")
        self.assertEqual(input.filename, "Sintel.2010.720p.mkv")
        self.assertEqual(input.inputType, "url")

'''
class TestEncodingProfile(unittest.TestCase):

    def test_create_encoding_profile(self):

        video_configs = list()

        video_config1 = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile="Main",
                                                   preset="standard", height=1024, width=768)
        video_config2 = bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile="Main",
                                                   preset="standard", height=480, width=320)
        video_configs.append(video_config1)
        video_configs.append(video_config2)

        audio_configs = list()

        audio_config = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)

        audio_configs.append(audio_config)

        encoding_profile = bitcodin.create_encoding_profile("API Test Profile", video_configs, audio_configs)
        print encoding_profile

    def test_create_job(self):

        input = bitcodin.create_input(url="http://ftp.nluug.nl/pub/graphics/blender/demo/movies/Sintel.2010.720p.mkv")

        video_configs = list()

        video_config1 = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile="Main",
                                                   preset="standard", height=1024, width=768)
        video_config2 = bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile="Main",
                                                   preset="standard", height=480, width=320)
        video_configs.append(video_config1)
        video_configs.append(video_config2)

        audio_configs = list()

        audio_config = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)

        audio_configs.append(audio_config)

        encoding_profile = bitcodin.create_encoding_profile("API Test Profile", video_configs, audio_configs)

        manifests = ["mpd", "m3u8"]
        job = bitcodin.create_job(input.inputId, encoding_profile.encodingProfileId, manifests)

        vars(job)
'''

if __name__ == '__main__':
    unittest.main()
