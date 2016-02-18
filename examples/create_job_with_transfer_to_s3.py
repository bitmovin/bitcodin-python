#!/usr/bin/env python
from time import sleep

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
print("INPUT REQUEST: %s\n\n" % input_obj.to_json())
input_result = bitcodin.create_input(input_obj)
print("INPUT RESULT: %s\n\n" % input_result.to_json())

video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1024000,
    profile='Main',
    preset='premium',
    height=768,
    width=1024
))
video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=1,
    bitrate=512000,
    profile='Main',
    preset='premium',
    height=480,
    width=640
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
    speed='standard'
)
print("JOB: %s" % job.to_json())

job_result = bitcodin.create_job(job)
while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print(job_result.to_json())
    sleep(5)

print(job_result.to_json())
print("Job Finished!")

output_obj = bitcodin.S3Output(
    name='MY S3 Output Profile',
    host='YOUR AWS HOST',
    access_key='YOUR AWS ACCESS KEY',
    secret_key='YOUR AWS SECRET KEY',
    bucket='YOUR AWS BUCKET NAME',
    prefix='PATH/TO/MY/DESIRED/OUTPUT/DESTINATION/',
    region='YOUR AWS REGION',
    make_public=False
)
output_result = bitcodin.create_output(output_obj)

print("Transferring job...")
transfer_job = bitcodin.transfer_job(job_result.job_id, output_result.output_id)
print("Transfer Job created: %s" % transfer_job)

print("Show transfer jobs...")
transfer_jobs = bitcodin.list_transfer_jobs(job_result.job_id)
for transfer in transfer_jobs:
    print("Transfer Job: %s" % transfer.to_json())
