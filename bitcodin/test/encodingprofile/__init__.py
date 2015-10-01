__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

from unittest import TestSuite

from .testcase_create_encoding_profile_incomplete_data import CreateEncodingProfileIncompleteDataTestCase
from .testcase_create_encoding_profile_invalid_data import CreateEncodingProfileInvalidDataTestCase
from .testcase_get_non_existent_encoding_profile import GetNonExistentEncodingProfileTestCase
from .testcase_create_encoding_profile import CreateEncodingProfileTestCase
from .testcase_get_encoding_profile import GetEncodingProfileTestCase
from .testcase_delete_encoding_profile import DeleteEncodingProfileTestCase
from .testcase_delete_non_existent_encoding_profile import DeleteNonExistentEncodingProfileTestCase
from .testcase_get_list_encoding_profiles import GetEncodingProfileListTestCase
from .testcase_create_encoding_profile_rotation import CreateEncodingProfileWithRotationTestCase

def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(CreateEncodingProfileIncompleteDataTestCase())
    test_suite.addTest(CreateEncodingProfileInvalidDataTestCase())
    test_suite.addTest(GetNonExistentEncodingProfileTestCase())
    test_suite.addTest(CreateEncodingProfileTestCase())
    test_suite.addTest(GetEncodingProfileTestCase())
    test_suite.addTest(DeleteEncodingProfileTestCase())
    test_suite.addTest(DeleteNonExistentEncodingProfileTestCase())
    test_suite.addTest(GetEncodingProfileListTestCase())
    test_suite.addTest(CreateEncodingProfileWithRotationTestCase())
    return test_suite
