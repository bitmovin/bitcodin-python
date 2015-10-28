__author__ = 'David Moser <david.moser@bitmovin.net>'

from unittest import TestSuite

from .testcase_create_delete_live_stream import CreateLiveStreamTestCase


def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(CreateLiveStreamTestCase())

    return test_suite
