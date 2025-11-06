import math

# def give_me_power(num):
#     return math.pow(num, 2)
#
# op=  give_me_power(10)
# print(op)

# num = int(input("Enter the number"))
# op2 = lambda num: math.pow(num, 2)
# print(op2(num))


op2 = lambda: math.pow(int(input("Enter the number")), 2)
print(op2())
