# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)
import math

# i/p - r - float
# o/p  -> string formatted output of area.


# Logic Building Formula
# || Step 1 ||
# Figure out the inputs and output
# input -> r ->  data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> String -> float - area , print area

# || Step 2 ||
# rough logic =  area = 3.14 * pow(r,2)


# || Step 3 ||
radius = float(input("Enter the radius of the circle\n"))
print(radius)
# area = 3.14987654 * (radius**2)
area = math.pi * pow(radius,2)

print("Area of the circle is -> ", area)

# String data formatting , Python f-strings, formatted string literals
print(f"Area of the circle is -> {area:.2f}")