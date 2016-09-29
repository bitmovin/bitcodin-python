__author__ = 'Jan Češpivo <jan.cespivo@coex.cz>'

import unittest

from bitcodin import Subscription
from bitcodin import list_events
from bitcodin import create_subscription
from bitcodin import list_subscriptions
from bitcodin import delete_subscription

from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetSubscriptionListTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetSubscriptionListTestCase, self).setUp()
        event = next((event for event in list_events() if event.name == 'encoding.finished'))
        subscription = Subscription(event_id=event.id, url='http://www.example.com/')
        self.created_subscription = create_subscription(subscription)

    def runTest(self):
        subscriptions = list_subscriptions()
        subscription_found = False
        for subscription in subscriptions:
            if self.created_subscription.id == subscription.id:
                subscription_found = True
                break
        self.assertEquals(subscription_found, True)

    def tearDown(self):
        delete_subscription(self.created_subscription.id)
        super(GetSubscriptionListTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
