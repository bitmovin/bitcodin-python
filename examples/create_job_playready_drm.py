#!/usr/bin/env python

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://eu-storage.bitcodin.com/inputs/Sintel.2010.720p.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = []
video_configs.append(bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
    preset='standard', height=1024, width=768))
video_configs.append(bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
    preset='standard', height=480, width=640))

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
