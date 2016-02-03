#!/usr/bin/env python
import bitcodin
import time
import sys
import datetime

# Set your API key
bitcodin.api_key = 'YOU API KEY'

# Create an output for your live stream data
date = datetime.datetime.today()
prefix = "%s%d%d%d%d%d%d" % ('livestream', date.year, date.month, date.day, date.hour, date.minute, date.second)

output = bitcodin.GCSOutput(
    name='Livesteam Output',
    access_key='Your GCS access key',
    secret_key='Your GCS secret key',
    bucket='Your bucket name',
    prefix=prefix,
    make_public=True
    )

output = bitcodin.create_output(output)

# Configure your live stream encoding profile

# Configure video representations
video_configs = list()

# 3 Mbit, 1920x1080, Full HD
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=3000000,
    profile='Main',
    preset='standard',
    height=1080,
    width=1920
))
# 1,5 Mbit, 1280x720, 720p
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1500000,
    profile='Main',
    preset='standard',
    height=720,
    width=1280
))
# 1 Mbit, 640x480, 480p
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1000000,
    profile='Main',
    preset='standard',
    height=480,
    width=640
))

# Configure audio representation
audio_configs = list()

# 256 kbps
audio_configs.append(bitcodin.AudioStreamConfig(
    default_stream_id=0,
    bitrate=256000
))

live_profile = bitcodin.EncodingProfile('Live Stream profile', video_configs, audio_configs)
live_profile = bitcodin.create_encoding_profile(live_profile)

# Create live stream
stream_key = "stream"
time_shift = 120
live_stream = bitcodin.LiveStream("test live stream",
                                  stream_key,
                                  live_profile.encoding_profile_id,
                                  time_shift,
                                  output.output_id)

live_stream = bitcodin.create_live_instance(live_stream)

print(live_stream.to_json())

# Wait until live stream is running and ready

while live_stream.status != 'RUNNING':
    live_stream = bitcodin.get_live_instance(live_stream.id)
    print(live_stream.to_json())
    if live_stream.status == 'ERROR':
        print("Error occurred during live stream creation!")
        sys.exit(-1)
    time.sleep(2)

print("Ready to stream.\nRTMP URL: %s\n" % live_stream.rtmp_push_url)
print("MPD URL: %s\nHLS URL: %s\nSTREAM KEY: %s\n" % (live_stream.mpd_url, live_stream.hls_url, live_stream.stream_key))

####################################################
# At this point you can stream to your live stream #
####################################################

################################################################################
# IMPORTANT! If you finished streaming don't forget to delete your live stream !
#
#
#
# bitcodin.delete_live_instance(live_stream.id)
#
# while live_stream.status != 'TERMINATED':
#     live_stream = bitcodin.get_live_instance(live_stream.id)
#     print(live_stream.to_json())
#     if live_stream.status == 'ERROR':
#         print("Error occurred during live stream deletion!")
#         sys.exit(-1)
#     time.sleep(2)
#################################################################################
