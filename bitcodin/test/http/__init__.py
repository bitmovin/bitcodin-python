__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

from unittest import TestSuite

from .testcase_get_undefined import HttpGetUndefinedTestCase
from .testcase_post_undefined import HttpPostUndefinedTestCase
from .testcase_delete_undefined import HttpDeleteUndefinedTestCase


def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(HttpGetUndefinedTestCase())
    test_suite.addTest(HttpPostUndefinedTestCase())
    test_suite.addTest(HttpDeleteUndefinedTestCase())
    return test_suite
