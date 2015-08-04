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
from .testcase_create_job_drm_invalid_config import CreateJobDrmInvalidConfigTestCase
from .testcase_create_job_drm import CreateJobDrmTestCase

def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(CreateJobInvalidDataTestCase())
    test_suite.addTest(CreateJobIncompleteDataTestCase())
    test_suite.addTest(CreateJobTestCase())
    test_suite.addTest(CreateJobDrmInvalidConfigTestCase())
    test_suite.addTest(CreateJobDrmTestCase())
    test_suite.addTest(GetNonExistentJobTestCase())
    test_suite.addTest(GetJobTestCase())
    test_suite.addTest(GetJobListTestCase())
    test_suite.addTest(GetJobStatusTestCase())
    test_suite.addTest(TransferJobToNonExistentOutputTestCase())
    test_suite.addTest(TransferJobToFTPTestCase())
    test_suite.addTest(TransferJobToS3TestCase())

    return test_suite
