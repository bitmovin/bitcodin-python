#!/usr/bin/env python
import bitcodin
import pprint

bitcodin.api_key = 'de93f6610ef1e8f5389b038f74946e2d0bda5d79f54d2e36b6af57618e696681'

live_instance = bitcodin.LiveInstance("test live stream")

live_instance_result = bitcodin.create_live_instance(live_instance)

pprint.pprint(live_instance_result)
