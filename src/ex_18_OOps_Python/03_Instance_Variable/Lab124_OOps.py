a = 10 # variable everywhere in the program
class Person:
    b = 11 # Instance variable

    def print_info(self):
        c = 20 #     Local variable
        print(c)
        print(self.b)
        print(a)


object_ref = Person()
#print(b)
#print(c)
