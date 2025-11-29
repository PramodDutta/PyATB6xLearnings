from collections import *

# # COUNTER - data s
# user_input = input("Enter a string")
# count_char = Counter(user_input)
# print(count_char)

# namedtuple
# info = ('Pramod', 34, True, 9.8)
# print(info)

info = namedtuple('info', ['name', 'age', 'ismarried', 'number'])
t = info('pramod', 34, True, 9.8)

print(t.name)
print(t.age)
print(t.ismarried)
print(t.number)
