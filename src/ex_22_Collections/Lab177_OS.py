import os

print(os.getcwd())
full_path = os.path.join(os.getcwd(),"pramod.txt")
# full_path = os.path.join("/Users/promode/PycharmProjects/PyATB6xLearning/src/ex_22_Collections","pramod.txt")
print(full_path)

file = open(full_path, 'r')
print(file.read())

