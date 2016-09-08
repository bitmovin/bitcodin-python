__author__ = 'Jan Češpivo <jan.cespivo@coex.cz>'

import unittest
from bitcodin import list_events
from bitcodin.test.bitcodin_test_case import BitcodinTestCase


class ListEventsTestCase(BitcodinTestCase):
    def runTest(self):
        events = list_events()
        for event in events:
            self.assertEquals(hasattr(event, 'id'), True)
            self.assertEquals(hasattr(event, 'name'), True)
            self.assertEquals(hasattr(event, 'description'), True)

if __name__ == '__main__':
    unittest.main()
