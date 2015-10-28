#!/usr/bin/env python

import unittest
from bitcodin.test.bitcodin_test_case import BitcodinTestCase

import bitcodin
import time


class CreateLiveStreamTestCase(BitcodinTestCase):

    def setUp(self):
        super(CreateLiveStreamTestCase, self).setUp()

    def runTest(self):

        encoding_profiles = bitcodin.list_encoding_profiles()
        outputs = bitcodin.list_outputs()

        self.assertIsNotNone(encoding_profiles)
        self.assertIsNotNone(outputs)
        self.assertGreaterEqual(len(encoding_profiles), 1)
        self.assertGreaterEqual(len(outputs), 1)

        output = None

        for o in outputs:
            if o.type == 'gcs':
                output = o
                break

        self.assertIsNotNone(output, 'No GCS output was found!')

        live_stream = bitcodin.LiveStream("test-live-stream",
                                          "stream",
                                          encoding_profiles[0].encoding_profile_id,
                                          120,
                                          output.output_id)

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
