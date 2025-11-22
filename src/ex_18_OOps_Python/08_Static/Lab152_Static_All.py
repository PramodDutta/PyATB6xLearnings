# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.

class O:
    @staticmethod
    def sum(a, b):
        return a + b

# t = O() - static methods can be accessed direclty.
print(O.sum(4,5))