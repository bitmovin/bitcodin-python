__author__ = 'David Moser <david.moser@bitmovin.net>'

import json
from rest import RestClient
from util import convert_dict
from decimal import *


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
    :return: BitcodinObject
    """
    url = get_api_base()+'/input/%d' % input_id
    res = RestClient.get(url=url, headers=create_headers())
    input_obj = BitcodinObject(res)

    return input_obj


def list_inputs(page=None):
    """
    Get a list of Inputs
    :param page: number of page to retrieve Inputs from
    :return: list
    """

    if page is None:
        url = get_api_base() + '/inputs'
    else:
        url = get_api_base()+'/inputs/%d' % page

    res = RestClient.get(url=url, headers=create_headers())
    input_obj = BitcodinObject(res)

    return input_obj.inputs


def delete_input(input_id=None):
    """
    Delete an input
    :param input_id: Id of the input to delete
    :return:
    """
    pass


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


def list_encoding_profiles(page=None):
    """
    List all encoding profiles
    :return: list
    """

    if page is None:
        url = get_api_base() + '/encoding-profiles'
    else:
        url = get_api_base()+'/encoding-profiles/%d' % page

    res = RestClient.get(url=url, headers=create_headers())
    encoding_profile_res = BitcodinObject(res)

    return encoding_profile_res.profiles


def delete_encoding_profile():
    """
    Delete an Encoding Profile
    :return:
    """
    pass


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


def list_jobs(page=None):
    """
    List all Jobs
    :return: list
    """

    if page is None:
        url = get_api_base() + '/jobs'
    else:
        url = get_api_base()+'/jobs/%d' % page

    res = RestClient.get(url=url, headers=create_headers())
    jobs_res = BitcodinObject(res)

    return jobs_res.jobs

def delete_job(job_id=None):
    """
    Delete a job
    :param job_id: The id of the job to delete
    :return:
    """
    pass


def create_output(output):
    """
    Create an output for bitcodin
    :param: Job: A Output object to create
    :return: BitcodinObject
    """

    res = RestClient.post(url=get_api_base()+'/output/create', headers=create_headers(), content=job.to_json())
    job = BitcodinObject(res)

    return job


def get_output(output_id=None):
    """
    Get information of a Job
    :param job_id: The id of the job to retrieve information from
    :return: Job
    """

    url = get_api_base()+'/job/%d' % job_id

    res = RestClient.get(url=url, headers=create_headers())
    job = BitcodinObject(res)

    return job


def list_outputs():
    """
    List all Jobs
    :return: list
    """
    pass


def delete_output(output_id=None):
    """
    Delete a job
    :param job_id: The id of the job to delete
    :return:
    """
    pass


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
        self.type = type

        if url is None:
            raise ValueError('url of Input can not be None')

        self.url = url

        super(Input, self).__init__(self.__dict__)


class Job(BitcodinObject):

    def __init__(self, input_id, encoding_profile_id, manifest_types):
        self.inputId = input_id
        self.encodingProfileId = encoding_profile_id
        self.manifestTypes = manifest_types

        super(Job, self).__init__(self.__dict__)


class EncodingProfile(BitcodinObject):

    def __init__(self, name='Encoding Profile', video_stream_configs=None, audio_stream_configs=None):

        self.name = name

        if video_stream_configs is None:
            raise ValueError('videoStreamConfigs can not be None')
        self.videoStreamConfigs = video_stream_configs

        if audio_stream_configs is None:
            raise ValueError('audioStreamConfigs can not be None')
        self.audioStreamConfigs = audio_stream_configs

        super(EncodingProfile, self).__init__(self.__dict__)


class VideoStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id=0, bitrate=1024000, profile='Main', preset='preset', height=480, width=640):
        self.defaultStreamId = default_stream_id
        self.bitrate = bitrate
        self.profile = profile
        self.preset = preset
        self.height = height
        self.width = width

        super(VideoStreamConfig, self).__init__(self.__dict__)


class AudioStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id=0, bitrate=1024000):
        self.defaultStreamId = default_stream_id
        self.bitrate = bitrate

        super(AudioStreamConfig, self).__init__(self.__dict__)
