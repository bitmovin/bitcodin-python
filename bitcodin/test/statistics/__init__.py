__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

from unittest import TestSuite
from .testcase_get_statistics_current import GetStatisticsCurrentMonthTestCase
from .testcase_get_statistics_from_to import GetStatisticsFromToTestCase


def get_test_suite():
    test_suite = TestSuite()
    #test_suite.addTest(GetStatisticsCurrentMonthTestCase())
    #test_suite.addTest(GetStatisticsFromToTestCase())

    return test_suite
