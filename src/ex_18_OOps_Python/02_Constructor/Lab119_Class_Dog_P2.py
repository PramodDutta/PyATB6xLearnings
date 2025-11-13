print("Outside the class")


class MobilePhone:
    model = None

    def __init__(self):
        print("DC")

    def talk(self):
        print("Hi,talking")


iphone = MobilePhone()
iphone.talk()
print("Outside the class2")
