# Task for the Today
# Take a 3 input from the user
# perform the sub, sub, mul and div

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
num3 = float(input("Enter a third number: "))

# Performing operations
sub_result = num1 - num2 - num3  # Subtracting second number from first
sum_result = num2 + num1 + num3  # Sub third number from secon
print(sub_result)
print(sum_result)


mul_result = num1 * num2 * num3  # Multiplying all three numbers
print(mul_result)

div_result = (num1 / num2) / num3  # Div all three numbers
print(div_result)