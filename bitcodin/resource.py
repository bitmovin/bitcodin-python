__author__ = 'David Moser <david.moser@bitmovin.net>'

import json
from .util import convert_dict


class BitcodinObject(dict):

    def __init__(self, dictionary):
        """
        :param dictionary: Result-Dictionary got from the bitcodin API

        Converts all dictionaries to BitcodinObject objects.
        """
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

    def __init__(self, input_id, encoding_profile_id, manifest_types, speed=None, drm_config=None,
                 hls_encryption_config=None, extract_closed_captions=False, audio_meta_data=None, video_meta_data=None):
        self.inputId = input_id
        self.encodingProfileId = encoding_profile_id
        self.manifestTypes = manifest_types
        if speed is not None:
            self.speed = speed
        if drm_config is not None:
            self.drmConfig = drm_config
        if hls_encryption_config is not None:
            self.hlsEncryptionConfig = hls_encryption_config
        if audio_meta_data is not None:
            self.audioMetaData = audio_meta_data
        if video_meta_data is not None:
            self.videoMetaData = video_meta_data

        super(Job, self).__init__(self.__dict__)


class DrmConfig(BitcodinObject):

    def __init__(self, system, method):
        self.system = system
        self.method = method

        super(DrmConfig, self).__init__(self.__dict__)


class AudioMetaData(BitcodinObject):

    def __init__(self, default_stream_id, language, label):
        self.defaultStreamId = default_stream_id
        self.language = language
        self.label = label

        super(BitcodinObject, self).__init__(self.__dict__)


class VideoMetaData(BitcodinObject):

    def __init__(self, default_stream_id, language, label):
        self.defaultStreamId = default_stream_id
        self.language = language
        self.label = label

        super(BitcodinObject, self).__init__(self.__dict__)


class WidevineDrmConfig(DrmConfig):

    def __init__(self, provider, signing_key, signing_iv, request_url, content_id, method):
        self.provider = provider
        self.signingKey = signing_key
        self.signingIV = signing_iv
        self.requestUrl = request_url
        self.contentId = content_id

        super(WidevineDrmConfig, self).__init__('widevine', method=method)


class PlayreadyDrmConfig(DrmConfig):

    def __init__(self, method, k_id, key=None, key_seed=None, la_url=None, lui_url=None, ds_id=None, custom_attributes=None):
        system = 'playready'
        self.kid = k_id
        if key is not None:
            self.key = key
        if key_seed is not None:
            self.keySeed = key_seed
        if la_url is not None:
            self.laUrl = la_url
        if lui_url is not None:
            self.luiUrl = lui_url
        if ds_id is not None:
            self.dsId = ds_id
        if custom_attributes is not None:
            self.customAttributes = custom_attributes

        super(PlayreadyDrmConfig, self).__init__(system=system, method=method)


class PlayreadyWidevineCombinedDrmConfig(DrmConfig):

    def __init__(self, method, key, pssh, kid, la_url=None, lui_url=None, ds_id=None, custom_attributes=None):
        system = 'widevine_playready'

        self.key = key
        self.pssh = pssh
        self.kid = kid
        if la_url is not None:
            self.laUrl = la_url
        if lui_url is not None:
            self.luiUrl = lui_url
        if ds_id is not None:
            self.dsId = ds_id
        if custom_attributes is not None:
            self.customAttributes = custom_attributes

        super(PlayreadyWidevineCombinedDrmConfig, self).__init__(system=system, method=method)


class HLSEncrpytionConfig(BitcodinObject):

    def __init__(self, key, method, iv=None):
        self.key = key
        self.method = method
        if iv is not None:
            self.iv = iv

        super(HLSEncrpytionConfig, self).__init__(self.__dict__)


class EncodingProfile(BitcodinObject):

    def __init__(self, name, video_stream_configs, audio_stream_configs):

        self.name = name
        self.videoStreamConfigs = video_stream_configs
        self.audioStreamConfigs = audio_stream_configs

        super(EncodingProfile, self).__init__(self.__dict__)


class VideoStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id, bitrate, profile, preset, height, width, frame_rate=None):
        self.defaultStreamId = default_stream_id
        self.bitrate = bitrate
        self.profile = profile
        self.preset = preset
        self.height = height
        self.width = width

        if frame_rate is not None:
            self.fps = frame_rate

        super(VideoStreamConfig, self).__init__(self.__dict__)


class AudioStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id, bitrate, sample_rate=None):
        self.defaultStreamId = default_stream_id
        self.bitrate = bitrate

        if sample_rate is not None:
            self.sampleRate = sample_rate

        super(AudioStreamConfig, self).__init__(self.__dict__)


class TransferConfig(BitcodinObject):

    def __init__(self, job_id, output_id):
        self.jobId = job_id
        self.outputId = output_id

        super(TransferConfig, self).__init__(self.__dict__)


class Output(BitcodinObject):

    def __init__(self, type, name, host):
        self.type = type
        self.name = name
        self.host = host

        super(Output, self).__init__(self.__dict__)


class S3Output(Output):

    def __init__(self, name, host, access_key, secret_key, bucket, prefix, region, make_public):
        self.type = 's3'
        self.name = name
        self.host = host
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucket = bucket
        self.prefix = prefix
        self.region = region
        self.makePublic = make_public

        super(S3Output, self).__init__(self.type, self.name, self.host)


class FTPOutput(Output):

    def __init__(self, name, host, basic_auth_user, basic_auth_password, passive=True):
        self.type = 'ftp'
        self.name = name
        self.host = host
        self.username = basic_auth_user
        self.password = basic_auth_password
        self.passive = passive

        super(FTPOutput, self).__init__(self.type, self.name, self.host)

