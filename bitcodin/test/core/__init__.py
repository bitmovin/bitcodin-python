__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

from unittest import TestSuite

from .testcase_api_key_authorized import ApiKeyAuthorizedTestCase
from .testcase_api_key_unauthorized import ApiKeyUnauthorizedTestCase
from .testcase_create_headers import CreateHttpHeadersTestCase
from .testcase_convert import ConvertTestCase
from .testcase_convert_dict import ConvertDictTestCase
from .testcase_get_api_base import GetApiBaseTestCase


def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(ConvertTestCase())
    test_suite.addTest(ConvertDictTestCase())
    test_suite.addTest(GetApiBaseTestCase())
    test_suite.addTest(CreateHttpHeadersTestCase())
    test_suite.addTest(ApiKeyAuthorizedTestCase())
    test_suite.addTest(ApiKeyUnauthorizedTestCase())
    return test_suite
