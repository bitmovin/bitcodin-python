__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

from unittest import TestSuite

from .testcase_create_job_invalid_data import CreateJobInvalidDataTestCase
from .testcase_create_job_incomplete_data import CreateJobIncompleteDataTestCase
from .testcase_create_job import CreateJobTestCase
from .testcase_get_job import GetJobTestCase
from .testcase_get_non_existent_job import GetNonExistentJobTestCase
from .testcase_get_list_jobs import GetJobListTestCase
from .testcase_get_job_status import GetJobStatusTestCase
from .testcase_transfer_job_to_non_existent_output import TransferJobToNonExistentOutputTestCase
from .testcase_transfer_job_ftp import TransferJobToFTPTestCase
from .testcase_transfer_job_s3 import TransferJobToS3TestCase
from .testcase_create_job_widevine_drm_invalid_config import CreateJobWidevineDrmInvalidConfigTestCase
from .testcase_create_job_widevine_drm import CreateJobWidevineDrmTestCase
from .testcase_create_job_playready_drm_invalid import CreateJobPlayreadyDrmInvalidConfigTestCase
from .testcase_create_job_playready_drm import CreateJobPlayreadyDrmTestCase
from .testcase_create_job_playready_widevine_drm_invalid import CreateJobPlayreadyWidevineDrmInvalidConfigTestCase
from .testcase_create_job_playready_widevine_drm import CreateJobPlayreadyWidevineDrmTestCase
from .testcase_create_job_hls_encryption import CreateJobHLSEncryptionTestCase
from .testcase_create_job_multiple_audio_streams import CreateJobWithMultipleAudioStreamsTestCase
from .testcase_create_job_azure_input import CreateJobAzureInputTestCase
from .testcase_create_job_s3_input import CreateJobS3InputTestCase
from .testcase_transfer_job_gcs import TransferJobToGCSTestCase
from .testcase_autotransfer_job_gcs import AutoTransferJobToGCSTestCase
from .testcase_autotransfer_job_ftp import AutoTransferJobToFTPTestCase
from .testcase_autotransfer_job_s3 import AutoTransferJobToS3TestCase
from .testcase_create_job_rotation import CreateJobWithRotationTestCase
from .testcase_create_job_specific_segment_length import CreateJobWithSpecificSegmentLengthTestCase
from .testcase_create_job_specific_video_audio_sample_rates import CreateJobWithSpecificVideoAndAudioSampleRatesTestCase
from .testcase_create_job_watermarked import CreateJobWithWatermarkTestCase
from .testcase_create_job_cropping_video import CreateJobWithVideoCroppingTestCase
from .testcase_transfer_job_azure import TransferJobToAzureTestCase
from .testcase_create_job_deinterlace import CreateJobWithDeinterlacing
from .testcase_create_job_mp3_audio_only import CreateJobAudioOnlyTestCase
from bitcodin.test.job.testcase_create_thumbnail import CreateThumbnailTestCase


def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(CreateJobInvalidDataTestCase())
    test_suite.addTest(CreateJobIncompleteDataTestCase())
    test_suite.addTest(CreateJobTestCase())
    test_suite.addTest(CreateJobWithMultipleAudioStreamsTestCase())
    test_suite.addTest(CreateJobHLSEncryptionTestCase())
    test_suite.addTest(CreateJobWidevineDrmInvalidConfigTestCase())
    test_suite.addTest(CreateJobWidevineDrmTestCase())
    test_suite.addTest(CreateJobPlayreadyDrmInvalidConfigTestCase())
    test_suite.addTest(CreateJobPlayreadyDrmTestCase())
    test_suite.addTest(CreateJobPlayreadyWidevineDrmInvalidConfigTestCase())
    test_suite.addTest(CreateJobPlayreadyWidevineDrmTestCase())
    test_suite.addTest(GetNonExistentJobTestCase())
    test_suite.addTest(GetJobTestCase())
    # TODO: fix test case to look up pages 2,3,4,5.... eventually the job list is so long that the job
    # TODO: is not in the first page anymore
    # test_suite.addTest(GetJobListTestCase())
    test_suite.addTest(GetJobStatusTestCase())
    test_suite.addTest(TransferJobToNonExistentOutputTestCase())
    test_suite.addTest(TransferJobToFTPTestCase())
    test_suite.addTest(TransferJobToS3TestCase())
    test_suite.addTest(CreateJobAzureInputTestCase())
    test_suite.addTest(CreateJobS3InputTestCase())
    test_suite.addTest(TransferJobToGCSTestCase())
    test_suite.addTest(AutoTransferJobToGCSTestCase())
    test_suite.addTest(AutoTransferJobToFTPTestCase())
    test_suite.addTest(AutoTransferJobToS3TestCase())
    test_suite.addTest(CreateJobWithRotationTestCase())
    test_suite.addTest(CreateJobWithSpecificSegmentLengthTestCase())
    test_suite.addTest(CreateJobWithSpecificVideoAndAudioSampleRatesTestCase())
    test_suite.addTest(CreateJobWithWatermarkTestCase())
    test_suite.addTest(CreateJobWithVideoCroppingTestCase())
    test_suite.addTest(TransferJobToAzureTestCase())
    test_suite.addTest(CreateJobWithDeinterlacing())
    test_suite.addTest(CreateJobAudioOnlyTestCase)
    test_suite.addTest(CreateThumbnailTestCase)

    return test_suite
