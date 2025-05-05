class TestCase:

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self,result):
        result.test_started()
        self.set_up()    # chama método de setup
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()    # chama método de teste 
        except AssertionError as e:
            result.add_failure(self.test_method_name)
        except Exception as e:
            result.add_error(self.test_method_name)
        self.tear_down() # chama método de teardown 

    def set_up(self):
        pass

    def tear_down(self):
        pass
