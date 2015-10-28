#!/usr/bin/env python
import bitcodin
import time
import sys

bitcodin.api_key = 'INSERT YOUR API KEY'

encoding_profiles = bitcodin.list_encoding_profiles()
outputs = bitcodin.list_outputs()
output = None

if len(outputs) <= 0:
    print "No outputs found!"
    sys.exit(-1)

for o in outputs:
    if o.type == 'gcs':
        output = o
        break

if output is None:
    print "No gcs output found!"
    sys.exit(-1)

live_stream = bitcodin.LiveStream("test live stream",
                                      "stream",
                                      encoding_profiles[0].encoding_profile_id,
                                      120,
                                      output.output_id)

live_stream = bitcodin.create_live_instance(live_stream)

print vars(live_stream)

while live_stream.status != 'RUNNING':
    live_stream = bitcodin.get_live_instance(live_stream.id)
    print vars(live_stream)
    if live_stream.status == 'ERROR':
        print "Error occurred during live stream creation!"
        sys.exit(-1)
    time.sleep(2)


bitcodin.delete_live_instance(live_stream.id)

while live_stream.status != 'TERMINATED':
    live_stream = bitcodin.get_live_instance(live_stream.id)
    print vars(live_stream)
    if live_stream.status == 'ERROR':
        print "Error occurred during live stream deletion!"
        sys.exit(-1)
    time.sleep(2)
