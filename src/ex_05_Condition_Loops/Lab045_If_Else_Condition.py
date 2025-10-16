# Problem to find the max between two.

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 31.4 or 45.34 - float

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

# if num1 > 0 and num2 > 0:
#     print("Number should be positive")

if num1 >= num2:
    print("Maximum", num1)
else:
    print("Maximum", num2)

# num1 == num2 ->  Handled.
