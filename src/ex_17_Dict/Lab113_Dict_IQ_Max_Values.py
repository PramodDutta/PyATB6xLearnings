# function that returns the maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}

# def min_value_dict(dictionary):
def max_value_dict(dictionary):
    # return min(dictionary.values())
    return max(dictionary.values())

def max_key_dict(dictionary):
    # return min(dictionary.values())
    return max(dictionary.keys())


# print(min_value_dict({"a": 10, "b": 20, "c": 30}))
print(max_value_dict({"a": 10, "b": 20, "c": 30}))
print(max_key_dict({"a": 10, "b": 20, "c": 30}))