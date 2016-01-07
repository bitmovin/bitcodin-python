#!/usr/bin/env python
from time import sleep

import bitcodin

# Set your API key
bitcodin.api_key = 'YOUR API KEY'

# Create an input
input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
input_result = bitcodin.create_input(input_obj)

# Create encoding profile
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

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

# Create a job
job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard'
)
job_result = bitcodin.create_job(job)
print("Job created!\n")

# Wait until job is finished
while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print(vars(job_result))
    sleep(5)

print(vars(job_result))
print("Job Finished!\n")

# Create a transmuxing job to generate files for progressive streaming
transmux_request = bitcodin.TransmuxRequest(job_result.job_id)
transmux_job = bitcodin.create_transmux_job(transmux_request)

while transmux_job.status != 'Finished' and transmux_job.status != 'Error':
    transmux_job = bitcodin.get_transmux_job(transmux_job.id)
    print(vars(transmux_job))
    sleep(5)

print(vars(transmux_job))
print("Transmuxing succeeded!\nURLs of output files:")
for url in transmux_job.files:
    print("%s\n" % url)
