__author__ = 'David Moser - david.moser@bitmovin.net'

#!/usr/bin/env python

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://url.to.video.with.closed.captions')
input_result = bitcodin.create_input(input_obj)

video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
                                                preset='standard', height=1024, width=768))
video_configs.append(bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=512000, profile='Main',
                                                preset='standard', height=480, width=640))

audio_configs = [
    bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000),
    bitcodin.AudioStreamConfig(default_stream_id=1, bitrate=192000)
]

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile Closed Captions', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

audio_meta_data = [
    bitcodin.AudioMetaData(0, 'Spanish', 'es'),
    bitcodin.AudioMetaData(1, 'English', 'en')
]

video_meta_data = [
    bitcodin.VideoMetaData(0, 'Spanish', 'es')
]

job = bitcodin.Job(input_result.input_id, encoding_profile_result.encoding_profile_id, manifests, None, None, None,
                   True, audio_meta_data, video_meta_data)
job_result = bitcodin.create_job(job)
