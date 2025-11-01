# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/O and O/P
# I/O -  int
# O/P - int

# Step 2 - Rough Logic
# return n1+n2+n3


# Step 3 - Write Logic

num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
num3 = int(input("Enter the third number\n"))


def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3


result = sum_of_three(num1, num2, num3)
result0 = sum_of_three(30, 40, 56)
result1 = sum_of_three()
result2 = sum_of_three(n1=10)
result3 = sum_of_three(n1=10, n2=30)
result4 = sum_of_three(n1=10, n2=30, n3=40)
result5 = sum_of_three(n3=num3)

print(result0)
print(result1)
print(result2)
print(result3)
print(result4)
print(result4)


def sum_of_three_numbers(a, b, c):
    return a + b + c


result1 = sum_of_three_numbers()
result2 = sum_of_three_numbers(30, 40, 50)
result3 = sum_of_three_numbers(a=1, b=2)
