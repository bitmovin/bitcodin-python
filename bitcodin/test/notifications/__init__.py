__author__ = 'Jan Češpivo <jan.cespivo@coex.cz>'

from unittest import TestSuite

from .testcase_get_list_events import ListEventsTestCase
from .testcase_get_list_subscriptions import GetSubscriptionListTestCase
from .testcase_get_subscription import GetSubscriptionTestCase
from .testcase_delete_subscription import DeleteSubscriptionTestCase


def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(ListEventsTestCase())
    test_suite.addTest(GetSubscriptionListTestCase())
    test_suite.addTest(GetSubscriptionTestCase())
    test_suite.addTest(DeleteSubscriptionTestCase())
    return test_suite
