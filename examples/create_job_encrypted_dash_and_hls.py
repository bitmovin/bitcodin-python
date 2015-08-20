#!/usr/bin/env python

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://eu-storage.bitcodin.com/inputs/Sintel.2010.720p.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = []
video_configs.append(bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
    preset='standard', height=480, width=640))

audio_configs = [bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=128000)]

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

drm_config = bitcodin.PlayreadyWidevineCombinedDrmConfig(
    key='100b6c20940f779a4589152b57d2dacb',
    pssh='CAESEOtnarvLNF6Wu89hZjDxo9oaDXdpZGV2aW5lX3Rlc3QiEGZrajNsamFTZGZhbGtyM2oqAkhEMgA=',
    kid='eb676abbcb345e96bbcf616630f1a3da',
    la_url='http://playready.directtaps.net/pr/svc/rightsmanager.asmx?PlayRight=1&ContentKey=EAtsIJQPd5pFiRUrV9Layw==',
    method='mpeg_cenc'
)

hls_encryption_config = bitcodin.HLSEncrpytionConfig(
    key='cab5b529ae28d5cc5e3e7bc3fd4a544d',
    method='SAMPLE-AES',
    iv='08eecef4b026deec395234d94218273d'
)

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard',
    drm_config=drm_config,
    hls_encryption_config=hls_encryption_config
)

job_result = bitcodin.create_job(job)
