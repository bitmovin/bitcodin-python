#!/usr/bin/env python

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
input_result = bitcodin.create_input(input_obj)

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

drm_config = bitcodin.PlayreadyDrmConfig(
    k_id='746573745f69645f4639465043304e4f',
    key_seed='XVBovsmzhP9gRIZxWfFta3VVRPzVEWmJsazEJ46I',
    la_url='http://playready.directtaps.net/pr/svc/rightsmanager.asmx',
    method='mpeg_cenc'
)

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard',
    drm_config=drm_config
)

job_result = bitcodin.create_job(job)
