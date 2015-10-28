import os

from testtools import ConcurrentStreamTestSuite, StreamToDict
from bitcodin.test import output

from bitcodin.test.settings import api_key

__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.net>'

import sys
from unittest import TestSuite, TextTestRunner
from . import core
from . import job
from . import http
from . import encodingprofile
from . import input
from . import statistics

VERBOSITY_LEVEL = 2


def _collect_test_suites():
    test_suites = list()
    test_suites.append(core.get_test_suite())
    test_suites.append(http.get_test_suite())
    test_suites.append(encodingprofile.get_test_suite())
    test_suites.append(input.get_test_suite())
    test_suites.append(job.get_test_suite())
    test_suites.append(statistics.get_test_suite())
    test_suites.append(output.get_test_suite())
    return test_suites


def _run_tests(test_suite):
    return TextTestRunner(verbosity=VERBOSITY_LEVEL).run(test_suite)


def callback(arg):
    global SUCCESS
    global FAILS
    global FAILED

    if "FAILS" not in globals():
        FAILS = 0
    if "SUCCESS" not in globals():
        SUCCESS = 0

    if "traceback" in arg["details"]:
        traceback = arg["details"]['traceback'].as_text()
        FAILED = True
        FAILS += 1
        print(arg["status"] + " " + traceback)
    else:
        traceback = ""
        SUCCESS += 1
        print("Success[" + str(SUCCESS) + "]")


# def main():
#     test_suites = _collect_test_suites()
#     main_test_suite = TestSuite()
#
#     for test_suite in test_suites:
#         main_test_suite.addTests(test_suite)
#
#     test_suite_result = _run_tests(main_test_suite)
#     if not test_suite_result.wasSuccessful():
#         sys.exit(1)


def main():
    os.environ["PYTHON_API_KEY"] = api_key

    test_suites = _collect_test_suites()
    main_test_suite = TestSuite()

    for test_suite in test_suites:
        main_test_suite.addTests(test_suite)

    concurrent_suite = ConcurrentStreamTestSuite(lambda: ((case, None) for case in main_test_suite))

    result = StreamToDict(callback)
    result.startTestRun()
    try:
        concurrent_suite.run(result)
    finally:
        result.stopTestRun()

    all = SUCCESS + FAILS
    print("All: " + str(all) + " SUCCESS: " + str(SUCCESS) + " FAILS: " + str(FAILS))

    if 'FAILED' in globals() and FAILED:
        sys.exit(1)


if __name__ == '__main__':
    main()
