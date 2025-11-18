class Home:
    def __init__(self):
        self.public_var = "father"
        self._protected_var = "brother"
        self.__private__var_dadsa__dasda__ = "baby"

    def mom(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("Private Wife")

object_ref = Home()
# object_ref.__wife()
# object_ref.__private_var

object_ref.mom()
# print(object_ref._protected_var)
# ⚠️ Technically accessible, but not recommended
