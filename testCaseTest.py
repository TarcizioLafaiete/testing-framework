from testCase import TestCase
from testStub import TestStub
from testResult import TestResult
from testSpy import TestSpy

class TestCaseTest(TestCase):

    def set_up(self):
        self.result = TestResult()

    def test_result_success_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        assert self.result.summary() == '1 run, 0 failed, 0 error'

    def test_result_failure_run(self):
        stub = TestStub('test_failure')
        stub.run(self.result)
        assert self.result.summary() == '1 run, 1 failed, 0 error'

    def test_result_error_run(self):
        stub = TestStub('test_error')
        stub.run(self.result)
        assert self.result.summary() == '1 run, 0 failed, 1 error'

    def test_result_multiple_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        stub = TestStub('test_failure')
        stub.run(self.result)
        stub = TestStub('test_error')
        stub.run(self.result)
        assert self.result.summary() == '3 run, 1 failed, 1 error'

    def test_was_set_up(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_set_up

    def test_was_run(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_run

    def test_was_tear_down(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_tear_down

    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.log == "set_up test_method tear_down"

    def test_assert_true(self):
        self.assert_true(True)  

    def test_assert_false(self):
        self.assert_false(False)

    def test_assert_equal(self):
        self.assert_equal("", "")
        self.assert_equal("foo", "foo")
        self.assert_equal([], [])
        self.assert_equal(['foo'], ['foo'])
        self.assert_equal((), ())
        self.assert_equal(('foo',), ('foo',))
        self.assert_equal({}, {})
        self.assert_equal({'foo'}, {'foo'})

    def test_assert_in(self):
        animals = {'monkey': 'banana', 'cow': 'grass', 'seal': 'fish'}

        self.assert_in('a', 'abc')
        self.assert_in('foo', ['foo'])
        self.assert_in(1, [1, 2, 3])
        self.assert_in('monkey', animals)



if __name__ == "__main__":
    result = TestResult()

    test = TestCaseTest('test_result_success_run')
    test.run(result)

    test = TestCaseTest('test_result_failure_run')
    test.run(result)

    test = TestCaseTest('test_result_error_run')
    test.run(result)

    test = TestCaseTest('test_result_multiple_run')
    test.run(result)

    test = TestCaseTest('test_was_set_up')
    test.run(result)

    test = TestCaseTest('test_was_run')
    test.run(result)

    test = TestCaseTest('test_was_tear_down')
    test.run(result)

    test = TestCaseTest('test_template_method')
    test.run(result)

    test = TestCaseTest("test_assert_true")
    test.run(result)

    test = TestCaseTest("test_assert_false")
    test.run(result)

    test = TestCaseTest("test_assert_equal")
    test.run(result)

    test = TestCaseTest("test_assert_in")
    test.run(result)

    print(result.summary())