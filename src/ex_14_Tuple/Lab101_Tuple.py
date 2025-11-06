cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(len(cities))
print("Paris" in cities)
print("New Delhi" in cities)

t = (12, 34, 56)
# t.append(12) # AttributeError: 'tuple' object has no attribute 'append'

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)

colors = ("red", "green", "blue")
for c in colors:
    print(c)

numbers = "Pramod" * 3
print(numbers)
numbers = (1, 2) * 3
print(numbers)

print(" ---------")

nums = (1, 2, 2, 3, 2)
print(len(nums))
print(nums.count(2))
print(nums.index(3))


my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)    # (1, 2, 3)

back_to_list = list(my_tuple)
print(back_to_list)   # [1, 2, 3]
print(max(back_to_list))   # [1, 2, 3]

my_list = [1, 2, 3]
print(my_list[0:2])
print(my_list[-1])
