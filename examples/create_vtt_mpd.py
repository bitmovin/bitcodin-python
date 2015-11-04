#!/usr/bin/env python
from time import sleep

import bitcodin

bitcodin.api_key = 'YOUR API KEY'

input_obj = bitcodin.Input(url='http://bitbucketireland.s3.amazonaws.com/Sintel-original-short.mkv')
input_result = bitcodin.create_input(input_obj)

video_configs = list()

video_configs.append(bitcodin.VideoStreamConfig(
    default_stream_id=0,
    bitrate=1024000,
    profile='Main',
    preset='standard',
    height=768,
    width=1024
))

audio_configs = [bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)]

encoding_profile_obj = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile_obj)

manifests = ['mpd', 'm3u8']

job = bitcodin.Job(
    input_id=input_result.input_id,
    encoding_profile_id=encoding_profile_result.encoding_profile_id,
    manifest_types=manifests
)
job_result = bitcodin.create_job(job)
print("Started Job with id %d\n" % job_result.job_id)

while job_result.status != 'Finished' and job_result.status != 'Error':
    job_result = bitcodin.get_job(job_result.job_id)
    print(vars(job_result))
    sleep(5)


subtitles = list()
sub_de = bitcodin.VttSubTitle('de', 'Deutsch', 'http://your.url/to/de_sub.vtt')
sub_eng = bitcodin.VttSubTitle('eng', 'English', 'http://your.url/to/eng_sub.vtt')
subtitles.append(sub_de)
subtitles.append(sub_eng)

vtt_mpd_request = bitcodin.VttMpdRequest(51, subtitles)

res = bitcodin.create_vtt_mpd(vtt_mpd_request)
print(res.mpd_url)
