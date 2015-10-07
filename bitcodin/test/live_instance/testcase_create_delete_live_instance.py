#!/usr/bin/env python

import unittest
from bitcodin.test.bitcodin_test_case import BitcodinTestCase

import bitcodin
import time


class CreateLiveInstanceTestCase(BitcodinTestCase):

    def setUp(self):
        super(CreateLiveInstanceTestCase, self).setUp()

    def runTest(self):

        encoding_profiles = bitcodin.list_encoding_profiles()
        outputs = bitcodin.list_outputs()

        self.assertIsNotNone(encoding_profiles)
        self.assertIsNotNone(outputs)
        self.assertGreaterEqual(len(encoding_profiles), 1)
        self.assertGreaterEqual(len(outputs), 1)
        self.assertEqual(outputs[0].type, 'gcs')

        live_instance = bitcodin.LiveInstance("test-live-stream",
                                              "stream",
                                              encoding_profiles[0].encoding_profile_id,
                                              30,
                                              outputs[0].output_id)

        live_instance = bitcodin.create_live_instance(live_instance)

        self.assertIsNotNone(live_instance.id)
        self.assertEqual(live_instance.status, 'STARTING')
        self.assertEqual(live_instance.stream_key, "stream")

        while live_instance.status != 'RUNNING' and live_instance.status != 'ERROR':
            live_instance = bitcodin.get_live_instance(live_instance.id)
            time.sleep(2)

        self.assertEqual(live_instance.status, 'RUNNING')
        self.assertIsNotNone(live_instance.created_at)

        bitcodin.delete_live_instance(live_instance.id)

        while live_instance.status != 'TERMINATED' and live_instance.status != 'ERROR':
            live_instance = bitcodin.get_live_instance(live_instance.id)
            time.sleep(2)

        self.assertEqual(live_instance.status, 'TERMINATED')
        self.assertIsNotNone(live_instance.terminated_at)


if __name__ == '__main__':
    unittest.main()
