#!/usr/bin/env python
from time import sleep

import bitcodin

bitcodin.api_key = 'INSERT YOUR API KEY HERE'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
print("INPUT REQUEST: %s\n\n" % input_obj.to_json())
input_result = bitcodin.create_input(input_obj)
print("INPUT RESULT: %s\n\n" % input_result.to_json())

video_configs = list()

# If height and width are given, aspect ratio will not be kept
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=4800000,
    profile='Main',
    preset='premium',
    height=600,
    width=1920
))

# If only width or only height is provided aspect ratio will be determined automatically
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=2400000,
    profile='Main',
    preset='premium',
    width=1024
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1200000,
    profile='Main',
    preset='premium',
    height=720
))

audio_configs = [bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)]

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
print("ENCODING PROFILE REQUEST %s\n\n" % encoding_profile_obj.to_json())

encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)
print("ENCODING PROFILE RESULT %s\n\n" % encoding_profile_result.to_json())

manifests = ['mpd', 'm3u8']

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='premium'
)
print("JOB: %s" % job.to_json())

job_result = bitcodin.create_job(job)
while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print(job_result.to_json())
    sleep(5)

print(job_result.to_json())
print("Job Finished!")