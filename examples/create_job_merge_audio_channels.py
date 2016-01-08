#!/usr/bin/env python
from time import sleep

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/at_test/mono_streams.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=512000,
    profile='Main',
    preset='standard',
    height=480,
    width=640
))

audio_configs = [
    bitcodin.AudioStreamConfig(
        default_stream_id=0,
        bitrate=192000
    )
]

encoding_profile_obj = bitcodin.EncodingProfile('Merge Audio Channels Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

# Merge all 6 audio channels into one
merge_audio_channel_config = bitcodin.MergeAudioChannelConfig([1, 2, 3, 4, 5, 6])
merge_audio_channel_configs = [merge_audio_channel_config]

manifests = ['mpd', 'm3u8']

# Audio merging is only available with speed standard
job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard',
    merge_audio_channel_configs=merge_audio_channel_configs
)
job_result = bitcodin.create_job(job)

while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print(vars(job_result))
    sleep(5)

print(vars(job_result))
print("Job Finished!")
