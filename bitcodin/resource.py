__author__ = 'David Moser <david.moser@bitmovin.net>'

import json
from rest import RestClient
from util import convert_dict


def create_input(input_obj):
    """
    Create an Input for bitcodin
    :param input_obj: Input object to create
    :return: Input
    """

    res = RestClient.post(url=get_api_base()+'/input/create', headers=create_headers(), content=input_obj.to_json())

    input_obj = BitcodinObject(res)

    return input_obj


def get_input(input_id=None):
    """
    Get Input information
    :param input_id: The id of the Input to retrieve info from
    :return: Input
    """
    url = get_api_base()+'/input/%d' % input_id
    res = RestClient.get(url=url, headers=create_headers())
    input_obj = BitcodinObject(res)

    return input_obj


def create_encoding_profile(encoding_profile):
    """
    Create an Encoding Profile for bitcodin.

    :param encoding_profile: EncodingProfile: EncodingProfile object to create
    :return: BitcodinObject
    """

    res = RestClient.post(url=get_api_base()+'/encoding-profile/create', headers=create_headers(),
                          content=encoding_profile.to_json())

    encoding_profile = BitcodinObject(res)

    return encoding_profile


def get_encoding_profile(encoding_profile_id=None):
    """
    Get information of an Encoding Profile
    :param encoding_profile_id: The id of the encoding profile to retrieve information from
    :return: BitcodinObject
    """

    url = get_api_base() + '/encoding-profile/%d' % encoding_profile_id
    res = RestClient.get(url=url, headers=create_headers())
    encoding_profile = BitcodinObject(res)

    return encoding_profile


def create_job(job):
    """
    Create a Job for bitcodin
    :param: Job: A Job object to create
    :return: BitcodinObject
    """

    res = RestClient.post(url=get_api_base()+'/job/create', headers=create_headers(), content=job.to_json())
    job = BitcodinObject(res)

    return job


def get_job(job_id=None):
    """
    Get information of a Job
    :param job_id: The id of the job to retrieve information from
    :return: Job
    """

    url = get_api_base()+'/job/%d' % job_id

    res = RestClient.get(url=url, headers=create_headers())
    job = BitcodinObject(res)

    return job


def get_api_base():
    """
    Get the api base url
    :return: string
    """
    from bitcodin import api_base
    return api_base


def create_headers():
    """
    Create standard headers to communicate with bitcodin-api
    :return:
    """
    from bitcodin import api_key

    if api_key is None:
        raise ValueError("api_key not set. Make sure you have set bitcodin.api_key")

    headers = {
        'Content-Type': 'application/json',
        'bitcodin-api-key': api_key
    }
    return headers


class BitcodinObject(dict):

    def __init__(self, dictionary):
        super(BitcodinObject, self).__init__()

        dictionary = convert_dict(dictionary)
        self.__dict__.update(dictionary)
        for k, v in dictionary.items():
            if isinstance(v, dict):
                self.__dict__[k] = BitcodinObject(v)
            if isinstance(v, list):
                index = 0
                for d in v:
                    v[index] = BitcodinObject(d)
                    index += 1
                del index

    def to_json(self):
        return json.dumps(self)

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError('No such attribute: ' + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError('No such attribute: ' + name)


class Input(BitcodinObject):

    def __init__(self, type="url", url=None):
        """
        :param type: string: Type of the Input
        :param url: string: Url to the source
        :return: Input
        """
        self.__setattr__('type', type)

        if url is None:
            raise ValueError('url of Input can not be None')

        self.__setattr__('url', url)

        super(Input, self).__init__(self.__dict__)


class Job(BitcodinObject):

    def __init__(self, input_id, encoding_profile_id, manifest_types):
        self.__setattr__('inputId', input_id)
        self.__setattr__('encodingProfileId', encoding_profile_id)
        self.__setattr__('manifestTypes', manifest_types)

        super(Job, self).__init__(self.__dict__)


class EncodingProfile(BitcodinObject):

    def __init__(self, name='Encoding Profile', video_stream_configs=None, audio_stream_configs=None):
        self.__setattr__('name', name)

        if video_stream_configs is None:
            raise ValueError('videoStreamConfigs can not be None')
        self.__setattr__('videoStreamConfigs', video_stream_configs)

        if audio_stream_configs is None:
            raise ValueError('audioStreamConfigs can not be None')
        self.__setattr__('audioStreamConfigs', audio_stream_configs)

        super(EncodingProfile, self).__init__(self.__dict__)


class VideoStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id=0, bitrate=1024000, profile='Main', preset='preset', height=480, width=204):
        self.__setattr__('defaultStreamId', default_stream_id)
        self.__setattr__('bitrate', bitrate)
        self.__setattr__('profile', profile)
        self.__setattr__('preset', preset)
        self.__setattr__('height', height)
        self.__setattr__('width', width)

        super(VideoStreamConfig, self).__init__(self.__dict__)


class AudioStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id=0, bitrate=1024000):
        self.__setattr__('defaultStreamId', default_stream_id)
        self.__setattr__('bitrate', bitrate)

        super(AudioStreamConfig, self).__init__(self.__dict__)
