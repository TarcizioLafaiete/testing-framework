from testLoader import TestLoader
from testCaseTest import TestCaseTest
from testSuiteTest import TestSuiteTest
from testLoaderTest import TestLoaderTest
from testSuite import TestSuite
from testRunner import TestRunner

if __name__ == "__main__":

    loader = TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_load_suite = loader.make_suite(TestLoaderTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TestRunner()
    runner.run(suite)