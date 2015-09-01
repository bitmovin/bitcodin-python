#!/usr/bin/env python

import unittest
from bitcodin.test.bitcodin_test_case import BitcodinTestCase

import bitcodin
import time
import sys


class CreateLiveInstanceTestCase(BitcodinTestCase):

    def setUp(self):
        super(CreateLiveInstanceTestCase, self).setUp()

    def runTest(self):

        live_instance = bitcodin.LiveInstance("test live stream")

        live_instance = bitcodin.create_live_instance(live_instance)

        while live_instance.status != 'RUNNING':
            live_instance = bitcodin.get_live_instance(live_instance.id)
            if live_instance.status == 'ERROR':
                print "Error occurred during live stream creation!"
                sys.exit(-1)
            time.sleep(2)

        bitcodin.delete_live_instance(live_instance.id)

        while live_instance.status != 'TERMINATED':
            live_instance = bitcodin.get_live_instance(live_instance.id)

            if live_instance.status == 'ERROR':
                print "Error occurred during live stream deletion!"
                sys.exit(-1)

            time.sleep(2)


if __name__ == '__main__':
    unittest.main()
