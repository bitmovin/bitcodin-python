#!/usr/bin/env python

import bitcodin

# Set your API key
bitcodin.api_key = 'INSERT YOUR API KEY'

# Create an input
input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
input_result = bitcodin.create_input(input_obj)

# Create encoding profile
video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=4800000,
    profile='Main',
    preset='premium',
    height=1080,
    width=1920
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=2400000,
    profile='Main',
    preset='premium',
    height=768,
    width=1024
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1200000,
    profile='Main',
    preset='premium',
    height=480,
    width=854
))

audio_configs = [bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)]

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

# Create a job
job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests
)
job_result = bitcodin.create_job(job)
print("Job created!")

# Create a thumbnail at second 50 with a height of 320px from a given job
# Note: You don't have to create a new job for a thumbnail, you can use finished jobs too.
thumbnail_request = bitcodin.ThumbnailRequest(job_id=job_result.job_id, height=320, position=50)
thumbnail = bitcodin.create_thumbnail(thumbnail_request)

print("Thumbnail generated!\nURL to thumbnail: %s\n" % thumbnail.thumbnail_url)

