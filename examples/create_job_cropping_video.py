#!/usr/bin/env python
from time import sleep

import bitcodin
import sys

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=4500000,
    profile='Main',
    preset='premium',
    height=818,
    width=1920
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=2400000,
    profile='Main',
    preset='premium',
    height=544,
    width=1280
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1000000,
    profile='Main',
    preset='premium',
    height=362,
    width=854
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=500000,
    profile='Main',
    preset='premium',
    height=272,
    width=640
))

audio_configs = [bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000, rate=48000)]

cropping_config = bitcodin.CroppingConfig(
    top=100,
    bottom=100,
    left=236,
    right=236
)

encoding_profile_obj = bitcodin.EncodingProfile(
    name='Cropping Profile',
    video_stream_configs=video_configs,
    audio_stream_configs=audio_configs,
    cropping_config=cropping_config
)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard'
)

try:
    job_result = bitcodin.create_job(job)
except Exception, e:
    print 'Could not start job: %s' % e.message
    print 'API Response: %s' % e.error
    sys.exit()

while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print(vars(job_result))
    sleep(5)

print(vars(job_result))
print("Job Finished!")
