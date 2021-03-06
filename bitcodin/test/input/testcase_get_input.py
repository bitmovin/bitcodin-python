__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
from bitcodin import create_input
from bitcodin import get_input
from bitcodin import delete_input
from bitcodin import Input
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetInputTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetInputTestCase, self).setUp()
        input_url = 'http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv'
        input = Input(input_url)
        self.created_input = create_input(input)

    def runTest(self):
        id = self.created_input.input_id
        input = get_input(id)
        self.assertEquals(self.created_input.input_id, input.input_id)
        self.assertEquals(self.created_input.filename, input.filename)
        self.assertEquals(self.created_input.created_at.date, input.created_at.date)
        self.assertEquals(self.created_input.created_at.timezone.timezone_type, input.created_at.timezone.timezone_type)
        self.assertEquals(self.created_input.created_at.timezone.timezone, input.created_at.timezone.timezone)
        self.assertEquals(self.created_input.updated_at.date, input.created_at.date)
        self.assertEquals(self.created_input.updated_at.timezone.timezone_type, input.created_at.timezone.timezone_type)
        self.assertEquals(self.created_input.updated_at.timezone.timezone, input.created_at.timezone.timezone)
        self.assertEquals(self.created_input.thumbnail_url, input.thumbnail_url)
        self.assertEquals(self.created_input.input_type, input.input_type)
        self.assertEquals(self.created_input.url, input.url)
        self.assertEquals(self.created_input.media_configurations[0].width, input.media_configurations[0].width)
        self.assertEquals(self.created_input.media_configurations[0].sample_aspect_ratio_num, input.media_configurations[0].sample_aspect_ratio_num)
        self.assertEquals(self.created_input.media_configurations[0].rate, input.media_configurations[0].rate)
        self.assertEquals(self.created_input.media_configurations[0].pixel_format, input.media_configurations[0].pixel_format)
        self.assertEquals(self.created_input.media_configurations[0].sample_aspect_ratio_den, input.media_configurations[0].sample_aspect_ratio_den)
        self.assertEquals(self.created_input.media_configurations[0].display_aspect_ratio_den, input.media_configurations[0].display_aspect_ratio_den)
        self.assertEquals(self.created_input.media_configurations[0].bitrate, input.media_configurations[0].bitrate)
        self.assertEquals(self.created_input.media_configurations[0].display_aspect_ratio_num, input.media_configurations[0].display_aspect_ratio_num)
        self.assertEquals(self.created_input.media_configurations[0].codec, input.media_configurations[0].codec)
        self.assertEquals(self.created_input.media_configurations[0].type, input.media_configurations[0].type)
        self.assertEquals(self.created_input.media_configurations[0].duration, input.media_configurations[0].duration)
        self.assertEquals(self.created_input.media_configurations[0].stream_id, input.media_configurations[0].stream_id)
        self.assertEquals(self.created_input.media_configurations[0].height, input.media_configurations[0].height)
        self.assertEquals(self.created_input.media_configurations[1].stream_id, input.media_configurations[1].stream_id)
        self.assertEquals(self.created_input.media_configurations[1].duration, input.media_configurations[1].duration)
        self.assertEquals(self.created_input.media_configurations[1].rate, input.media_configurations[1].rate)
        self.assertEquals(self.created_input.media_configurations[1].codec, input.media_configurations[1].codec)
        self.assertEquals(self.created_input.media_configurations[1].type, input.media_configurations[1].type)
        self.assertEquals(self.created_input.media_configurations[1].bitrate, input.media_configurations[1].bitrate)
        self.assertEquals(self.created_input.media_configurations[1].sample_format, input.media_configurations[1].sample_format)
        self.assertEquals(self.created_input.media_configurations[1].channel_format, input.media_configurations[1].channel_format)

    def tearDown(self):
        delete_input(self.created_input.input_id)
        super(GetInputTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
