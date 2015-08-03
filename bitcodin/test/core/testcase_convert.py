__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

from bitcodin.util import convert
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class ConvertTestCase(BitcodinTestCase):
    def setUp(self):
        super(ConvertTestCase, self).setUp()

    def runTest(self):
        camel_case = 'pythonsDontEatCamels'
        snake_case = convert(camel_case)
        self.assertEqual(snake_case, 'pythons_dont_eat_camels')

    def tearDown(self):
        super(ConvertTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
