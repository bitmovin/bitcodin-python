__author__ = 'Jan Češpivo <jan.cespivo@coex.cz>'

import unittest

from bitcodin import Subscription
from bitcodin import list_events
from bitcodin import create_subscription
from bitcodin import delete_subscription

from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class DeleteSubscriptionTestCase(BitcodinTestCase):
    def setUp(self):
        super(DeleteSubscriptionTestCase, self).setUp()
        event = next((event for event in list_events() if event.name == 'encoding.finished'))
        subscription = Subscription(event_id=event.id, url='http://www.example.com/')
        self.created_subscription = create_subscription(subscription)

    def runTest(self):
        delete_subscription(self.created_subscription.id)

    def tearDown(self):
        super(DeleteSubscriptionTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
