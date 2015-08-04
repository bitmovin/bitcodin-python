__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

from unittest import TestSuite

from .testcase_create_s3_output_incomplete import CreateS3OutputIncompleteDataTestCase
from .testcase_create_s3_output_invalid import CreateS3OutputInvalidDataTestCase
from .testcase_create_s3_output import CreateS3OutputTestCase
from .testcase_get_s3_output import GetS3OutputTestCase
from .testcase_create_ftp_output_incomplete import CreateFTPOutputIncompleteDataTestCase
from .testcase_create_ftp_output_invalid import CreateFTPOutputInvalidDataTestCase
from .testcase_create_ftp_output import CreateFTPOutputTestCase
from .testcase_get_ftp_output import GetFTPOutputTestCase
from .testcase_get_non_existent_output import GetNonExistentOutputTestCase
from .testcase_delete_s3_output import DeleteS3OutputTestCase
from .testcase_delete_ftp_output import DeleteFTPOutputTestCase


def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(CreateS3OutputIncompleteDataTestCase())
    test_suite.addTest(CreateS3OutputInvalidDataTestCase())
    test_suite.addTest(CreateS3OutputTestCase())
    test_suite.addTest(GetS3OutputTestCase())
    test_suite.addTest(CreateFTPOutputIncompleteDataTestCase())
    test_suite.addTest(CreateFTPOutputInvalidDataTestCase())
    test_suite.addTest(CreateFTPOutputTestCase())
    test_suite.addTest(GetFTPOutputTestCase())
    test_suite.addTest(GetNonExistentOutputTestCase())
    test_suite.addTest(DeleteS3OutputTestCase())
    test_suite.addTest(DeleteFTPOutputTestCase())

    return test_suite
