#!/usr/bin/env python
import bitcodin
import time
import sys
import datetime

# SET YOUR API KEY
bitcodin.api_key = 'YOU API KEY'

# CREATE OUTPUT FOR YOUR LIVE STREAM DATA
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

# CONFIGURE YOUR LIVE STREAM ENCODING PROFILE

# CONFIGURE VIDEO REPRESENTATIONS
video_configs = list()

# 3 MBIT, 1920x1080, FULL HD
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=3000000,
    profile='Main',
    preset='standard',
    height=1080,
    width=1920
))
# 1,5 MBIT, 1280x720, 720p
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1500000,
    profile='Main',
    preset='standard',
    height=720,
    width=1280
))
# 1 MBIT, 640x480, 480p
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1000000,
    profile='Main',
    preset='standard',
    height=480,
    width=640
))

# CONFIGURE AUDIO REPRESENTATION
audio_configs = list()

# 256 kbps
audio_configs.append(bitcodin.AudioStreamConfig(
    default_stream_id=0,
    bitrate=256000
))

live_profile = bitcodin.EncodingProfile('Live Stream profile', video_configs, audio_configs)
live_profile = bitcodin.create_encoding_profile(live_profile)

# CREATE LIVE STREAM
stream_key = "stream"
time_shift = 120
live_stream = bitcodin.LiveStream("test live stream",
                                  stream_key,
                                  live_profile.encoding_profile_id,
                                  time_shift,
                                  output.output_id)

live_stream = bitcodin.create_live_instance(live_stream)

print(vars(live_stream))

# WAIT UNTIL LIVE STREAM IS RUNNING AND READY

while live_stream.status != 'RUNNING':
    live_stream = bitcodin.get_live_instance(live_stream.id)
    print(vars(live_stream))
    if live_stream.status == 'ERROR':
        print("Error occurred during live stream creation!")
        sys.exit(-1)
    time.sleep(2)

print("Ready to stream.\nRTMP URL: %s\n" % live_stream.rtmp_push_url)
print("MPD URL: %s\nHLS URL: %s\nSTREAM KEY: %s\n" % (live_stream.mpd_url, live_stream.hls_url, live_stream.stream_key))

####################################################
# AT THIS POINT YOU CAN STREAM TO YOUR LIVE STREAM #
####################################################

################################################################################
# IMPORTANT! IF YOU FINISHED STREAMING DON'T FORGET TO DELETE YOUR LIVE STREAM
#
#
#
# bitcodin.delete_live_instance(live_stream.id)
#
# while live_stream.status != 'TERMINATED':
#     live_stream = bitcodin.get_live_instance(live_stream.id)
#     print(vars(live_stream))
#     if live_stream.status == 'ERROR':
#         print("Error occurred during live stream deletion!")
#         sys.exit(-1)
#     time.sleep(2)
#################################################################################
