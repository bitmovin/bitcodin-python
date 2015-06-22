__author__ = 'David Moser <david.moser@bitmovin.net>'

import json
from rest import RestClient


def create_input(type="url", url=None):
    input_obj = Input(type, url)
    res = RestClient.post(url=get_api_base()+'/input/create', headers=create_headers(), content=input_obj.to_json())

    input_obj = BitcodinObject(res)

    return input_obj

def get_input(input_id=None):

    res = RestClient.get(url=get_api_base()+'/input/'+input_id, headers=create_headers())
    input_obj = BitcodinObject(res)

    return input_obj

def create_encoding_profile(name="Encoding Profile", video_stream_configs=None, audio_stream_configs=None):

    encoding_profile = EncodingProfile(name, video_stream_configs, audio_stream_configs)

    res = RestClient.post(url=get_api_base()+'/encoding-profile/create', headers=create_headers(),
                          content=encoding_profile.to_json())

    encoding_profile = BitcodinObject(res)

    return encoding_profile

def get_encoding_profile(encoding_profile_id=None):

    res = RestClient.get(url=get_api_base()+'/encoding-profile/'+encoding_profile_id, headers=create_headers())
    encoding_profile = BitcodinObject(res)

    return encoding_profile


def create_job(input_id=1, encoding_profile_id=1, manifest_types=None):
    job = Job(input_id, encoding_profile_id, manifest_types)

    res = RestClient.post(url=get_api_base()+'/job/create', headers=create_headers(), content=job.to_json())
    job = BitcodinObject(res)

    return job

def get_job(job_id=None):

    res = RestClient.get(url=get_api_base()+'/job/'+job_id, headers=create_headers())
    job = BitcodinObject(res)

    return job

def get_api_base():
    from bitcodin import api_base
    return api_base


def create_headers():
    from bitcodin import api_key

    if api_key is None:
        raise ValueError("api_key not set. Make sure you have set bitcodin.api_key")

    headers = {
        'Content-Type': 'application/json',
        'bitcodin-api-key': api_key
    }
    return headers


class BitcodinObject(dict):

    def to_json(self):
        return json.dumps(self)

    def from_json(self, json_string):
        print json_string

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)

class Input(BitcodinObject):

    def __init__(self, type="url", url=None):
        super(Input, self).__init__()

        self.__setattr__("type", type)

        if url is None:
            raise ValueError("url of Input can not be None")

        self.__setattr__("url", url)


class Job(BitcodinObject):

    def __init__(self, input_id, encoding_profile_id, manifest_types):
        super(Job, self).__init__()

        self.__setattr__("inputId", input_id)
        self.__setattr__("encodingProfileId", encoding_profile_id)
        self.__setattr__("manifestTypes", manifest_types)


class EncodingProfile(BitcodinObject):

    def __init__(self, name="Encoding Profile", video_stream_configs=None, audio_stream_configs=None):
        super(EncodingProfile, self).__init__()

        self.__setattr__("name", name)

        if video_stream_configs is None:
            raise ValueError("videoStreamConfigs can not be None")
        self.__setattr__("videoStreamConfigs", video_stream_configs)

        if audio_stream_configs is None:
            raise ValueError("audioStreamConfigs can not be None")
        self.__setattr__("audioStreamConfigs", audio_stream_configs)


class VideoStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id=0, bitrate=1024000, profile="Main", preset="preset", height=480, width=204):
        super(VideoStreamConfig, self).__init__()

        self.__setattr__("defaultStreamId", default_stream_id)
        self.__setattr__("bitrate", bitrate)
        self.__setattr__("profile", profile)
        self.__setattr__("preset", preset)
        self.__setattr__("height", height)
        self.__setattr__("width", width)


class AudioStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id=0, bitrate=1024000):
        super(AudioStreamConfig, self).__init__()

        self.__setattr__("defaultStreamId", default_stream_id)
        self.__setattr__("bitrate", bitrate)


