#!/usr/bin/env python

import unittest
from bitcodin.test.bitcodin_test_case import BitcodinTestCase

import bitcodin
import time


class CreateLiveInstanceTestCase(BitcodinTestCase):

    def setUp(self):
        super(CreateLiveInstanceTestCase, self).setUp()

    def runTest(self):

        live_instance = bitcodin.LiveInstance("test live stream")

        live_instance = bitcodin.create_live_instance(live_instance)
        self.assertIsNotNone(live_instance.id)
        self.assertEqual(live_instance.status, 'STARTING')

        while live_instance.status != 'RUNNING' or live_instance.status != 'ERROR':
            live_instance = bitcodin.get_live_instance(live_instance.id)
            time.sleep(2)

        self.assertEqual(live_instance.status, 'RUNNING')
        self.assertIsNotNone(live_instance.created_at)
        self.assertIsInstance(live_instance, bitcodin.LiveInstance)

        bitcodin.delete_live_instance(live_instance.id)

        while live_instance.status != 'TERMINATED' or live_instance.status != 'ERROR':
            live_instance = bitcodin.get_live_instance(live_instance.id)
            time.sleep(2)

        self.assertEqual(live_instance.status, 'TERMINATED')
        self.assertIsNotNone(live_instance.terminated_at)


if __name__ == '__main__':
    unittest.main()
