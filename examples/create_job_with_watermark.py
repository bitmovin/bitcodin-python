#!/usr/bin/env python
from time import sleep

import bitcodin
import sys

bitcodin.api_key = '0a609aa814e73e7b0470524dc5ecb5a393b2fe60d064c7bcb69db1cd7e719af8'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1024000,
    profile='Main',
    preset='standard',
    height=768,
    width=1024
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=1,
    bitrate=512000,
    profile='Main',
    preset='standard',
    height=480,
    width=640
))

audio_configs = [bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)]

watermark_config = bitcodin.WatermarkConfig(
    image_url='http://bitdash-a.akamaihd.net/webpages/bitcodin/images/bitcodin-bitmovin-logo-small.png',
    bottom=200,
    right=100
)

encoding_profile_obj = bitcodin.EncodingProfile(
    name='API Test Profile',
    video_stream_configs=video_configs,
    audio_stream_configs=audio_configs,
    watermark_config=watermark_config
)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests
)

try:
    job_result = bitcodin.create_job(job)
except Exception, e:
    print 'Could not start job: %s' % e.message
    print 'API Response: %s' % e.error
    sys.exit()

while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print vars(job_result)
    sleep(5)

print vars(job_result)
print "Job Finished!"
