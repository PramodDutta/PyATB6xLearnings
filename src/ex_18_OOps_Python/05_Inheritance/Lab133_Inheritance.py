# Single Inheritance
# A Subclass/Child/Son inherits from one Parent/Base/Father.


class BaseTest:
    driver = "Chrome"
    __driver2 = "FF"

    def setup(self):
        print("Base setup with the browser and env"+self.__driver2)


class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running the Testcases -> " + self.driver)


t = LoginTest()
t.run()
