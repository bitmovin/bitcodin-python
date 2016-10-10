import json
from .util import convert_dict

__author__ = 'David Moser <david.moser@bitmovin.net>'


class BitcodinObject(dict):

    def __init__(self, dictionary, convert=False):
        """
        Converts all dictionaries to BitcodinObject objects.
        """
        super(BitcodinObject, self).__init__()

        if convert:
            self.__dict__.update(convert_dict(dictionary))
        else:
            self.__dict__.update(dictionary)

        self.to_object(convert)

    def to_object(self, convert=False):
        for k, v in self.__dict__.items():
            if isinstance(v, dict):
                self.__dict__[k] = BitcodinObject(v, convert)

            elif isinstance(v, list):
                index = 0
                for d in v:
                    if isinstance(d, dict):
                        v[index] = BitcodinObject(d, convert)
                    else:
                        v[index] = d
                    index += 1
                del index
                self.__dict__[k] = v

            else:
                self.__dict__[k] = v

    def to_dict(self):
        for k, v in self.__dict__.items():
            if isinstance(v, BitcodinObject):
                setattr(self, k, v.to_dict())

            elif isinstance(v, list):
                index = 0
                for d in v:
                    if isinstance(d, BitcodinObject):
                        v[index] = d.to_dict()
                    index += 1
                del index

        return self.__dict__

    def to_json(self):
        json_string = json.dumps(self.to_dict())
        self.to_object()
        return json_string

    def __repr__(self):
        return repr(self.__dict__)

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError('No such attribute: %s' % name)

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError('No such attribute: ' + name)

    def __bool__(self):
        return bool(self.__dict__)

    def __len__(self):
        return len(self.__dict__)


class Input(BitcodinObject):

    def __init__(self, url, skip_analysis=False, username=None, password=None):
        """
        :param url: string: Url to the source (Allowed protocols: http(s))
        :param skip_analysis: boolean: Skip analysis of video
        :param username: string: HTTP Basic Auth username
        :param password: string: HTTP Basic Auth password
        :return: Input
        """
        self.type = 'url'
        self.url = url
        self.skipAnalysis = skip_analysis
        self.username = username
        self.password = password

        super(Input, self).__init__(self.to_dict())


class FTPInput(BitcodinObject):

    def __init__(self, url, skip_analysis=False, username=None, password=None):
        """
        :param url: string: Url to the source (Allowed protocols: (s)ftp)
        :param skip_analysis: boolean: Skip analysis of video
        :param username: string: (s)ftp username
        :param password: string: (s)ftp password
        :return: Input
        """
        self.type = 'ftp'
        self.url = url
        self.skipAnalysis = skip_analysis
        self.username = username
        self.password = password

        super(FTPInput, self).__init__(self.to_dict())


class S3Input(BitcodinObject):

    def __init__(self, access_key, secret_key, bucket, region, object_key, host=None, skip_analysis=False):
        """

        :param access_key: AWS Access Key ID
        :param secret_key: AWS Secret Key
        :param bucket: AWS Bucket Name
        :param region: AWS Region
        :param object_key: Path to object/file
        :param host: AWS Host (optional)
        :param skip_analysis: boolean: Skip analysis of video
        :return: S3Input
        """

        self.type = 's3'

        if host is not None:
            self.host = host
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucket = bucket
        self.region = region
        self.objectKey = object_key
        self.skipAnalysis = skip_analysis

        super(S3Input, self).__init__(self.to_dict())


class AzureInput(BitcodinObject):

    def __init__(self, account_name, account_key, container, url, skip_analysis=False):
        """

        :param account_name: Azure Account Name
        :param account_key: Azure Account Key
        :param container: Container Name
        :param url: URL to file/object
        :param skip_analysis: boolean: Skip analysis of video
        :return: AzureInput
        """

        self.type = 'abs'
        self.accountName = account_name
        self.accountKey = account_key
        self.container = container
        self.url = url
        self.skipAnalysis = skip_analysis

        super(AzureInput, self).__init__(self.to_dict())


class Job(BitcodinObject):

    def __init__(self, input_id, encoding_profile_id, manifest_types, speed=None, drm_config=None,
                 hls_encryption_config=None, extract_closed_captions=False, audio_meta_data=None, video_meta_data=None,
                 location=None, output_id=None, deinterlace=None, merge_audio_channel_configs=None, duration=None,
                 start_time=None):
        self.inputId = input_id
        self.encodingProfileId = encoding_profile_id
        self.manifestTypes = manifest_types
        self.extractClosedCaptions = extract_closed_captions

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
        if location is not None:
            self.location = location
        if output_id is not None:
            self.outputId = output_id
        if deinterlace is not None:
            self.deinterlace = deinterlace
        if merge_audio_channel_configs is not None:
            self.mergeAudioChannelConfigs = merge_audio_channel_configs
        if duration is not None:
            self.duration = duration
        if start_time is not None:
            self.startTime = start_time

        super(Job, self).__init__(self.to_dict())


class DrmConfig(BitcodinObject):

    def __init__(self, system, method):
        self.system = system
        self.method = method

        super(DrmConfig, self).__init__(self.to_dict())


class AudioMetaData(BitcodinObject):

    def __init__(self, default_stream_id, language, label):
        self.defaultStreamId = default_stream_id
        self.language = language
        self.label = label

        super(BitcodinObject, self).__init__(self.to_dict())


class VideoMetaData(BitcodinObject):

    def __init__(self, default_stream_id, language, label):
        self.defaultStreamId = default_stream_id
        self.language = language
        self.label = label

        super(BitcodinObject, self).__init__(self.to_dict())


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


class HLSEncryptionConfig(BitcodinObject):

    def __init__(self, key, method, iv=None, uri=None):
        self.key = key
        self.method = method
        if iv is not None:
            self.iv = iv
        if uri is not None:
            self.uri = uri

        super(HLSEncryptionConfig, self).__init__(self.to_dict())


class EncodingProfile(BitcodinObject):

    def __init__(self, name, video_stream_configs, audio_stream_configs, rotation=0, segment_length=None, watermark_config=None, cropping_config=None):

        self.name = name
        self.videoStreamConfigs = video_stream_configs
        self.audioStreamConfigs = audio_stream_configs
        self.rotation = rotation
        if segment_length is not None:
            self.segmentLength = segment_length
        if watermark_config is not None:
            self.watermarkConfig = watermark_config
        if cropping_config is not None:
            self.croppingConfig = cropping_config

        super(EncodingProfile, self).__init__(self.to_dict())


class VideoStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id, bitrate, profile, preset, height=None, width=None, rate=None, codec=None):
        self.defaultStreamId = default_stream_id
        self.bitrate = bitrate
        self.profile = profile
        self.preset = preset

        if height is not None:
            self.height = height

        if width is not None:
            self.width = width

        if rate is not None:
            self.rate = rate

        if codec is not None:
            self.codec = codec

        super(VideoStreamConfig, self).__init__(self.to_dict())


class AudioStreamConfig(BitcodinObject):

    def __init__(self, default_stream_id, bitrate, rate=None):
        self.defaultStreamId = default_stream_id
        self.bitrate = bitrate

        if rate is not None:
            self.rate = rate

        super(AudioStreamConfig, self).__init__(self.to_dict())


class WatermarkConfig(BitcodinObject):

    def __init__(self, image_url, top=None, bottom=None, left=None, right=None):
        self.image = image_url
        if top is not None:
            self.top = top
        if bottom is not None:
            self.bottom = bottom
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

        super(WatermarkConfig, self).__init__(self.to_dict())


class CroppingConfig(BitcodinObject):

    def __init__(self, top=None, bottom=None, left=None, right=None):
        if top is not None:
            self.top = top
        if bottom is not None:
            self.bottom = bottom
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

        super(CroppingConfig, self).__init__(self.to_dict())


class TransferConfig(BitcodinObject):

    def __init__(self, job_id, output_id):
        self.jobId = job_id
        self.outputId = output_id

        super(TransferConfig, self).__init__(self.to_dict())


class Output(BitcodinObject):

    def __init__(self, type, name, create_sub_directory=True):
        self.type = type
        self.name = name
        self.createSubDirectory = create_sub_directory

        super(Output, self).__init__(self.to_dict())


class S3Output(Output):

    def __init__(self, name, host, access_key, secret_key, bucket, prefix, region, make_public,
                 create_sub_directory=True):
        self.host = host
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucket = bucket
        self.prefix = prefix
        self.region = region
        self.makePublic = make_public

        super(S3Output, self).__init__('s3', name, create_sub_directory)


class FTPOutput(Output):

    def __init__(self, name, host, basic_auth_user, basic_auth_password, passive=True, create_sub_directory=True):
        self.host = host
        self.username = basic_auth_user
        self.password = basic_auth_password
        self.passive = passive

        super(FTPOutput, self).__init__('ftp', name, create_sub_directory)


class SFTPOutput(Output):

    def __init__(self, name, host, usename, password, passive=True, create_sub_directory=True):
        self.host = host
        self.username = usename
        self.password = password
        self.passive = passive

        super(SFTPOutput, self).__init__('sftp', name, create_sub_directory)


class GCSOutput(Output):

    def __init__(self, name, access_key, secret_key, bucket, prefix, make_public=False, create_sub_directory=True):
        self.accessKey = access_key
        self.secretKey = secret_key
        self.bucket = bucket
        self.prefix = prefix
        self.makePublic = make_public

        super(GCSOutput, self).__init__('gcs', name, create_sub_directory)


class AzureOutput(Output):

    def __init__(self, name, account_name, account_key, container, prefix, create_sub_directory=True):
        self.accountName = account_name
        self.accountKey = account_key
        self.container = container
        self.prefix = prefix

        super(AzureOutput, self).__init__('azure', name, create_sub_directory)


class LiveStream(BitcodinObject):

    def __init__(self, label, stream_key, encoding_profile_id, timeshift, output_id):
        self.label = label
        self.streamKey = stream_key
        self.encodingProfileId = encoding_profile_id
        self.timeshift = timeshift
        self.outputId = output_id

        super(LiveStream, self).__init__(self.to_dict())


class VttSubTitle(BitcodinObject):

    def __init__(self, lang_short, lang_long, url):
        self.langLong = lang_long
        self.langShort = lang_short
        self.url = url

        super(VttSubTitle, self).__init__(self.to_dict())


class VttMpdRequest(BitcodinObject):

    def __init__(self, job_id, subtitles):
        self.jobId = job_id
        self.subtitles = subtitles

        super(VttMpdRequest, self).__init__(self.__dict__)


class ThumbnailRequest(BitcodinObject):

    def __init__(self, job_id, height, position, filename=None):
        self.jobId = job_id
        self.height = height
        self.position = position
        self.async = True

        if filename is not None:
            self.filename = filename

        super(ThumbnailRequest, self).__init__(self.__dict__)

class SpriteRequest(BitcodinObject):

    def __init__(self, job_id, height, width, distance, filename=None):
        self.jobId = job_id
        self.height = height
        self.width = width
        self.distance = distance
        self.async = True

        if filename is not None:
            self.filename = filename

        super(SpriteRequest, self).__init__(self.__dict__)

class TransmuxRequest(BitcodinObject):

    def __init__(self, job_id):
        self.jobId = job_id
        super(TransmuxRequest, self).__init__(self.__dict__)


class MergeAudioChannelConfig(BitcodinObject):

    def __init__(self, audio_channels=None):
        if not audio_channels:
            audio_channels = []
        self.audioChannels = audio_channels
        super(MergeAudioChannelConfig, self).__init__(self.__dict__)


class TransmuxingConfig(BitcodinObject):

    def __init__(self, job_id=None, video_representation_id=None, audio_representation_ids=None, filename=None):
        if not audio_representation_ids:
            audio_representation_ids = []

        self.audioRepresentationIds = audio_representation_ids
        self.videoRepresentationId = video_representation_id
        self.jobId = job_id

        if filename is not None:
            self.filename = filename

        super(TransmuxingConfig, self).__init__(self.__dict__)


class Subscription(BitcodinObject):
    def __init__(self, event_id, url):
        self.eventId = event_id
        self.url = url

        super(Subscription, self).__init__(self.__dict__)
