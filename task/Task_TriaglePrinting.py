# *
# * *
# * * *
# n = 3

rows = int(input("Enter the rows for the Right Angle Triangle"))

for i in range(1, rows + 1):
    for j in range(i):
        print("*",end="")
    print()
