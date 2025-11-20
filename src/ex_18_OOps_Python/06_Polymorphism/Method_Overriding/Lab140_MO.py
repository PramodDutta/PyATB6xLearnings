class BaseTest:
    def run(self):
        print("Running generic test")


class LoginTest(BaseTest):

    def run(self):
        print("Running Login Test")


# t = LoginTest()
t = BaseTest()
t.run()
