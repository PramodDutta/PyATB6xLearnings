num = int(input("Enter a number which fact you want to get!"))
# 5
fact = 1

if num < 0:
    print("Fact is not defined!")

if num == 0:
    print("FACT = ", fact)
else:
    for i in range(1, num + 1):
        fact = fact * i

print("Factorial of : ", fact)
