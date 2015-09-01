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
    test_suite.addTest(GetJobListTestCase())
    test_suite.addTest(GetJobStatusTestCase())
    test_suite.addTest(TransferJobToNonExistentOutputTestCase())
    test_suite.addTest(TransferJobToFTPTestCase())
    test_suite.addTest(TransferJobToS3TestCase())

    return test_suite
