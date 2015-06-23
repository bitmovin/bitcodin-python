# [![bitcodin](http://www.bitcodin.com/wp-content/uploads/2014/10/bitcodin-small.gif)](http://www.bitcodin.com)
[![Build Status](https://travis-ci.org/bitmovin/bitcodin-python.svg?branch=master)](https://travis-ci.org/bitmovin/bitcodin-python)
[![Coverage Status](https://coveralls.io/repos/bitmovin/bitcodin-python/badge.svg?branch=master)](https://coveralls.io/r/bitmovin/bitcodin-python?branch=master)

The bitcodin API for Python is a seamless integration with the [bitcodin cloud transcoding system](http://www.bitcodin.com). It enables the generation of MPEG-DASH and HLS content in just some minutes.

Installation
------------

### Install with pip ###

```
pip install bitcodin
```
 
Usage
-----

Before you can start using the api you need to **set your API key.**

Your API key can be found in the **settings of your bitcodin user account**, as shown in the figure below.

![APIKey](http://www.bitcodin.com/wp-content/uploads/2015/06/api_key.png)

An example how you can set the bitcodin API is shown in the following:

```python
import bitcodin
bitcodin.api_key = 'yourapikey'
```

Example
-----
The following example demonstrates how to create a simple transcoding job:
```python

import bitcodin

bitcodin.api_key = 'yourapikey'
input_obj = bitcodin.Input(url='http://www.example.com/yourfolder/yourmovie.mp4')
        input_result = bitcodin.create_input(input_obj)

        video_configs = list()
        video_config1 = bitcodin.VideoStreamConfig(default_stream_id=0, bitrate=1024000, profile='Main',
                                                   preset='standard', height=1024, width=768)
        video_config2 = bitcodin.VideoStreamConfig(default_stream_id=1, bitrate=512000, profile='Main',
                                                   preset='standard', height=480, width=320)
        video_configs.append(video_config1)
        video_configs.append(video_config2)

        audio_configs = list()
        audio_config = bitcodin.AudioStreamConfig(default_stream_id=0, bitrate=192000)
        audio_configs.append(audio_config)

        encoding_profile = bitcodin.EncodingProfile('API Test Profile', video_configs, audio_configs)
        encoding_profile_result = bitcodin.create_encoding_profile(encoding_profile)

        manifests = ['mpd', 'm3u8']

        job = bitcodin.Job(input_result.input_id, encoding_profile_result.encoding_profile_id, manifests)
        job_result = bitcodin.create_job(job)

```