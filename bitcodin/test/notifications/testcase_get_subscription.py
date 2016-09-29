__author__ = 'Jan Češpivo <jan.cespivo@coex.cz>'

import unittest

from bitcodin import Subscription
from bitcodin import list_events
from bitcodin import get_subscription
from bitcodin import create_subscription
from bitcodin import delete_subscription

from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class GetSubscriptionTestCase(BitcodinTestCase):
    def setUp(self):
        super(GetSubscriptionTestCase, self).setUp()
        event = next((event for event in list_events() if event.name == 'encoding.finished'))
        subscription = Subscription(event_id=event.id, url='http://www.example.com/')
        self.created_subscription = create_subscription(subscription)

    def runTest(self):
        subscription_id = self.created_subscription.id
        subscription = get_subscription(subscription_id)
        self.assertEquals(self.created_subscription, subscription)

    def tearDown(self):
        delete_subscription(self.created_subscription.id)
        super(GetSubscriptionTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
