#• Create a list that stores only positive num from given list.

num = [-5, 3, -2, 7, 0, 4]
def is_positive(x):
    return x > 0
print("given list : ",num)
print("Using filter and a function")
pves = list(filter(is_positive, num))
print(pves)
print("Using filter and a lambda")
pves = list(filter(lambda x: x > 0, num))
print(pves)
print("Using list comprehension")
pves = [x for x in num if x > 0]
print(pves)

