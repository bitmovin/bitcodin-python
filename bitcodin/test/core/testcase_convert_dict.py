__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import unittest

from bitcodin.util import convert_dict
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class ConvertDictTestCase(BitcodinTestCase):
    def setUp(self):
        super(ConvertDictTestCase, self).setUp()

    def runTest(self):
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

    def tearDown(self):
        super(ConvertDictTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
