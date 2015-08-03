__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import sys
from unittest import TestSuite, TextTestRunner
from . import core
from . import http
from . import encodingprofile
from . import input

VERBOSITY_LEVEL = 2

def _collect_test_suites():
    test_suites = []
    test_suites.append(core.get_test_suite())
    test_suites.append(http.get_test_suite())
    test_suites.append(encodingprofile.get_test_suite())
    test_suites.append(input.get_test_suite())
    return test_suites

def _run_tests(test_suite):
    return TextTestRunner(verbosity=VERBOSITY_LEVEL).run(test_suite)


def main():
    test_suites = _collect_test_suites()
    main_test_suite = TestSuite()

    test_suite_results = []
    for test_suite in test_suites:
        main_test_suite.addTests(test_suite)
        #test_suite_results.append(_run_tests(test_suite))

    test_suite_results.append(_run_tests(main_test_suite))

if __name__ == '__main__':
    main()
