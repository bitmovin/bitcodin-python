#!/usr/bin/env python

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = list()
video_configs.append(bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
                                                preset='premium', height=1024, width=768))
video_configs.append(bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
                                                preset='premium', height=480, width=640))

audio_configs = [bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)]

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

hls_encryption_config = bitcodin.HLSEncryptionConfig(
    key='cab5b529ae28d5cc5e3e7bc3fd4a544d',
    method='SAMPLE-AES',
    iv='08eecef4b026deec395234d94218273d'
)

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard',
    hls_encryption_config=hls_encryption_config
)

job_result = bitcodin.create_job(job)
