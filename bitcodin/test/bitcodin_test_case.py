__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest
import bitcodin
from bitcodin.test.settings import api_key


class BitcodinTestCase(unittest.TestCase):
    def setUp(self):
        bitcodin.api_key = api_key

    def tearDown(self):
        bitcodin.api_key = None

