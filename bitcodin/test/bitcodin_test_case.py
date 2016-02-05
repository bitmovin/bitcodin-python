from time import sleep

import unittest
import bitcodin
from bitcodin.test.settings import api_key
from bitcodin import get_job

__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'


class BitcodinTestCase(unittest.TestCase):
    def setUp(self):
        bitcodin.api_key = api_key

    def tearDown(self):
        bitcodin.api_key = None

    def wait_until_job_finished(self, job_id):
        job_result = get_job(job_id)

        while job_result.status != 'Finished':
            job_result = get_job(job_result.job_id)
            self.assertNotEqual(job_result.status, 'Error')
            print(job_result.to_json())
            sleep(5)
