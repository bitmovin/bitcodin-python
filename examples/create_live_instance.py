#!/usr/bin/env python
import bitcodin
import time
import sys

bitcodin.api_key = 'INSERT YOUR API KEY'

encoding_profiles = bitcodin.list_encoding_profiles()

live_instance = bitcodin.LiveInstance("test live stream", "stream", encoding_profiles[0].encoding_profile_id, 30)

live_instance = bitcodin.create_live_instance(live_instance)

print vars(live_instance)

while live_instance.status != 'RUNNING':
    live_instance = bitcodin.get_live_instance(live_instance.id)
    print vars(live_instance)
    if live_instance.status == 'ERROR':
        print "Error occurred during live stream creation!"
        sys.exit(-1)
    time.sleep(2)


bitcodin.delete_live_instance(live_instance.id)

while live_instance.status != 'TERMINATED':
    live_instance = bitcodin.get_live_instance(live_instance.id)
    print vars(live_instance)
    if live_instance.status == 'ERROR':
        print "Error occurred during live stream deletion!"
        sys.exit(-1)
    time.sleep(2)
