__author__ = 'David Moser <david.moser@bitmovin.net>'

import json
from util import convert_dict


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

    def __init__(self, url=None):
        """
        :param url: string: Url to the source
        :return: Input
        """
        self.type = 'url'
        self.url = url

        super(Input, self).__init__(self.__dict__)


class Job(BitcodinObject):

    def __init__(self, input_id=None, encoding_profile_id=None, manifest_types=None):
        self.inputId = input_id
        self.encodingProfileId = encoding_profile_id
        self.manifestTypes = manifest_types

        super(Job, self).__init__(self.__dict__)


class EncodingProfile(BitcodinObject):

    def __init__(self, name='Encoding Profile', video_stream_configs=None, audio_stream_configs=None):

        self.name = name
        self.videoStreamConfigs = video_stream_configs
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


class Output(BitcodinObject):

    def __init__(self, type, name, host, access_key, secret_key, bucket, prefix, region, make_public):
        self.type = type
        self.name = name
        self.host = host
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucket = bucket
        self.prefix = prefix
        self.region = region
        self.make_public = make_public

        super(Output, self).__init__(self.__dict__)