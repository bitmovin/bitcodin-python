#!/usr/bin/env python

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-two-audio-streams-short.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = []
video_stream_config = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=512000,
                                                 profile='Main', preset='premium', height=480, width=640)
video_configs.append(video_stream_config)

audio_configs = []
audio_stream_config_0 = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)
audio_stream_config_1 = bitcodin.AudioStreamConfig(default_stream_id=1, bitrate=192000)
audio_configs.append(audio_stream_config_0)
audio_configs.append(audio_stream_config_1)

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

audio_meta_data = []
audio_stream_config_0_meta_data = bitcodin.AudioMetaData(0, 'de', 'Just Sound')
audio_stream_config_1_meta_data = bitcodin.AudioMetaData(1, 'en', 'Sound and Voice')
audio_meta_data.append(audio_stream_config_0_meta_data)
audio_meta_data.append(audio_stream_config_1_meta_data)

manifests = ['mpd', 'm3u8']

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests,
    speed='standard',
    audio_meta_data=audio_meta_data
)

job_result = bitcodin.create_job(job)
