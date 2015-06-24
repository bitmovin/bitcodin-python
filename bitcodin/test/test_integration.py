from bitcodin.test import settings

__author__ = 'David Moser <david.moser@bitmovin.net>'

import unittest

import bitcodin
from bitcodin.util import convert, convert_dict
from requests.exceptions import HTTPError

bitcodin.api_key = settings.api_key


class TestInput(unittest.TestCase):

    def test_create_input(self):

        input_obj = bitcodin.Input(url='http://ftp.nluug.nl/pub/graphics/blender/demo/movies/Sintel.2010.720p.mkv')
        input_response = bitcodin.create_input(input_obj)

        self.assertEqual(input_response.url, 'http://ftp.nluug.nl/pub/graphics/blender/demo/movies/Sintel.2010.720p.mkv')
        self.assertEqual(input_response.filename, 'Sintel.2010.720p.mkv')
        self.assertEqual(input_response.input_type, 'url')

    def test_create_input_wrong_parameter(self):
        input_obj = bitcodin.Input()
        with self.assertRaises(HTTPError):
            bitcodin.create_input(input_obj)

    def test_get_input(self):
        inputs = bitcodin.list_inputs()

        self.assertGreater(len(inputs), 0)

        single_input = bitcodin.get_input(inputs[0].input_id)
        self.assertEqual(inputs[0].input_id, single_input.input_id)

    def test_delete_input(self):
        inputs = bitcodin.list_inputs()
        self.assertGreater(len(inputs), 0)
        self.assertTrue(bitcodin.delete_input(inputs[0].input_id))


class TestEncodingProfile(unittest.TestCase):

    def test_create_encoding_profile(self):

        video_configs = list()
        video_config1 = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
                                                   preset='standard', height=768, width=1024)
        video_config2 = bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
                                                   preset='standard', height=480, width=640)
        video_configs.append(video_config1)
        video_configs.append(video_config2)

        audio_configs = list()
        audio_config = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)
        audio_configs.append(audio_config)

        encoding_profile = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
        encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile)

        self.assertEqual(encoding_profile_result.name, 'API Test Profile')

    def test_get_encoding_profile(self):

        encoding_profiles = bitcodin.list_encoding_profiles()
        self.assertGreater(len(encoding_profiles), 0)

        single_encoding_profile = bitcodin.get_encoding_profile(encoding_profiles[0].encoding_profile_id)
        self.assertEqual(single_encoding_profile.encoding_profile_id, encoding_profiles[0].encoding_profile_id)


class TestJob(unittest.TestCase):

    def test_create_job(self):

        input_obj = bitcodin.Input(url='http://ftp.nluug.nl/pub/graphics/blender/demo/movies/Sintel.2010.720p.mkv')
        input_result = bitcodin.create_input(input_obj)

        video_configs = list()
        video_config1 = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
                                                   preset='standard', height=768, width=1024)
        video_config2 = bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
                                                   preset='standard', height=480, width=640)
        video_configs.append(video_config1)
        video_configs.append(video_config2)

        audio_configs = list()
        audio_config = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)
        audio_configs.append(audio_config)

        encoding_profile = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
        encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile)

        manifests = ['mpd', 'm3u8']

        job = bitcodin.Job(input_result.input_id, encoding_profile_result.encoding_profile_id, manifests)

        job_result = bitcodin.create_job(job)
        self.assertEqual(job_result.status, 'Enqueued')

    def test_get_job(self):
        jobs = bitcodin.list_jobs()
        self.assertGreater(len(jobs), 0)

        single_job = bitcodin.get_job(jobs[0].job_id)
        self.assertEqual(jobs[0].job_id, single_job.job_id)


class TestOutput(unittest.TestCase):

    def test_create_s3_output(self):
        output = bitcodin.S3Output(
            'Api Test S3 Output',
            settings.aws_config['host'],
            settings.aws_config['access_key'],
            settings.aws_config['secret_key'],
            settings.aws_config['bucket'],
            settings.aws_config['prefix'],
            settings.aws_config['region'],
            True
        )

        output_result = bitcodin.create_output(output)

        self.assertEqual(output_result.type, 's3')
        self.assertTrue(output_result.make_public)

    def test_create_ftp_output(self):
        output = bitcodin.FTPOutput(
            'API Test FTP Output',
            settings.ftp_config['host'],
            settings.ftp_config['username'],
            settings.ftp_config['password'],
            True
        )

        output_result = bitcodin.create_output(output)

        self.assertEqual(output_result.type, 'ftp')

    def test_get_output(self):
        outputs = bitcodin.list_outputs()
        self.assertGreater(len(outputs), 0)

        single_output = bitcodin.get_output(outputs[0].output_id)
        self.assertEqual(single_output.output_id, outputs[0].output_id)

    def test_delete_output(self):
        outputs = bitcodin.list_outputs()
        self.assertGreater(len(outputs), 0)
        self.assertTrue(bitcodin.delete_output(outputs[0].output_id))


class TestUtil(unittest.TestCase):

    def test_convert(self):
        camel_case = 'pythonsDontEatCamels'
        snake_case = convert(camel_case)
        self.assertEqual(snake_case, 'pythons_dont_eat_camels')

    def test_convert_dict(self):
        d = {
            'camelCaseAttr': 'camelCaseContent',
            'AnotherCamel': 'CamelContent',
            'camelCamel': '_Camel'
        }
        converted = {
            'camel_case_attr': 'camelCaseContent',
            'another_camel': 'CamelContent',
            'camel_camel': '_Camel'
        }

        snake_dict = convert_dict(d)
        self.assertDictEqual(converted, snake_dict)


class TestMethods(unittest.TestCase):

    def test_create_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'bitcodin-api-key': bitcodin.api_key
        }
        header_created = bitcodin.create_headers()

        self.assertDictEqual(headers, header_created)

    def test_get_api_base(self):
        api_base = bitcodin.api_base
        api_base_got = bitcodin.get_api_base()

        self.assertEqual(api_base, api_base_got)

if __name__ == '__main__':
    unittest.main()
