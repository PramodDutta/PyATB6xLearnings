# Find the positive number is even or odd
num = int(input("Enter a number: ").strip())

if num >= 0:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative Number")



if num >= 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Negative Number")

# You can write short one-liner conditions using ternary operator:
