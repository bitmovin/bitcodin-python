#!/usr/bin/env python
import bitcodin
import pprint
import sys

live_instance = bitcodin.LiveInstance("test live stream")

live_instance = bitcodin.create_live_instance(live_instance)

pprint.pprint(live_instance)

while live_instance.status != 'RUNNING':
    live_instance = bitcodin.get_live_instance(live_instance.id)
    if live_instance.status == 'ERROR':
        print "Error occurred during live stream creation!"
        sys.exit(-1)


bitcodin.delete_live_instance(live_instance.id)

while live_instance.status != 'TERMINATED':
    live_instance = bitcodin.get_live_instance(live_instance.id)
    if live_instance.status == 'ERROR':
        print "Error occurred during live stream deletion!"
        sys.exit(-1)