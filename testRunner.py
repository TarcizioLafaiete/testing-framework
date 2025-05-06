from testResult import TestResult
from testLoader import TestLoader
from testLoaderTest import TestLoaderTest

class TestRunner:

    def __init__(self):
        self.result = TestResult()

    def run(self, test):
        test.run(self.result)
        print(self.result.summary())
        return self.result
    
if __name__ == "__main__":
    loader = TestLoader()
    suite = loader.make_suite(TestLoaderTest)

    runner = TestRunner()
    runner.run(suite)