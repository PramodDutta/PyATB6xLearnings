dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.keys())
print(dict1.values())

dict2 = {"a": 1, "b": 2}

missing_keys = set(dict1.keys() - dict2.keys())
print(missing_keys)
