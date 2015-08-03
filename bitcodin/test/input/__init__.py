__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

from unittest import TestSuite

from .testcase_create_input_incomplete_data import CreateInputIncompleteDataTestCase
from .testcase_create_input_invalid_data import CreateInputInvalidDataTestCase
from .testcase_create_input import CreateInputTestCase
from .testcase_get_input import GetInputTestCase
from .testcase_get_non_existent_input import GetNonExistentInputTestCase
from .testcase_get_list_inputs import GetInputListTestCase
from .testcase_delete_non_existent_input import DeleteNonExistentInputTestCase
from .testcase_delete_input import DeleteInputTestCase
from .testcase_analyze_non_existent_input import AnalyzeNonExistentInputTestCase
from .testcase_analyze_input import AnalyzeInputTestCase

def get_test_suite():
    test_suite = TestSuite()
    test_suite.addTest(CreateInputIncompleteDataTestCase())
    test_suite.addTest(CreateInputInvalidDataTestCase())
    test_suite.addTest(CreateInputTestCase())
    test_suite.addTest(GetInputTestCase())
    test_suite.addTest(GetNonExistentInputTestCase())
    test_suite.addTest(GetInputListTestCase())
    test_suite.addTest(DeleteNonExistentInputTestCase())
    test_suite.addTest(DeleteInputTestCase())
    test_suite.addTest(AnalyzeNonExistentInputTestCase())
    test_suite.addTest(AnalyzeInputTestCase())
    return test_suite
