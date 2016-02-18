#!/usr/bin/env python
from time import sleep

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

# This file has 6 audio channels
input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/at_test/mono_streams.mkv')
input_result = bitcodin.create_input(input_obj)

# Create your video and audio configurations for your encoding
video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=512000,
    profile='Main',
    preset='premium',
    height=480,
    width=640
))

# The result are two audio streams so we have to configure it also in the encoding profile
audio_configs = [
    bitcodin.AudioStreamConfig(
        default_stream_id=0,
        bitrate=192000
    ),
    bitcodin.AudioStreamConfig(
        default_stream_id=1,
        bitrate=128000
    )
]

# Create the encoding profile
encoding_profile_obj = bitcodin.EncodingProfile('Merge Audio Channels Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

# MERGE CONFIGURATION

# Merge audio channel 1 and 2 audio streams
merge_audio_channel_config12 = bitcodin.MergeAudioChannelConfig([1, 2])

# Merge audio channel 3 and 4
merge_audio_channel_config34 = bitcodin.MergeAudioChannelConfig([3, 4])

# This results in two stereo audio channels

merge_audio_channel_configs = [merge_audio_channel_config12, merge_audio_channel_config34]

# Create audio meta data
audio_meta_data12 = bitcodin.AudioMetaData(0, 'en', 'Channel 1 and 2 merged')
audio_meta_data34 = bitcodin.AudioMetaData(1, 'en', 'Channel 3 and 4 merged')
audio_meta_data = [audio_meta_data12, audio_meta_data34]

manifests = ['mpd', 'm3u8']

# Create the job
# Audio merging is only available with speed standard
job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard',
    merge_audio_channel_configs=merge_audio_channel_configs,
    audio_meta_data=audio_meta_data
)
job_result = bitcodin.create_job(job)

while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print(job_result.to_json())
    sleep(5)

print(job_result.to_json())
print("Job Finished!")
