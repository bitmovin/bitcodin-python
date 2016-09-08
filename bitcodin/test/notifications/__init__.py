__author__ = 'Jan Češpivo <jan.cespivo@coex.cz>'

from unittest import TestSuite

from .testcase_get_list_events import ListEventsTestCase


def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(ListEventsTestCase())

    return test_suite
