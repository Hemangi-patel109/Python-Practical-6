from functools import reduce

def find_max(x, y):
    return x if x > y else y
numbers = [31, 5, 70, 2, 18, 71, 1, 4]
max_value = reduce(find_max, numbers)
print(f"The maximum value in the list is: {max_value}")
