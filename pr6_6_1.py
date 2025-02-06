# Create a list to store the cube of all the elements in a given list.

numbers = [1, 2, 3, 4]

def cube(x):
    return x**3
print("cube list of ",numbers)
print("Using map and a function")
cubes = list(map(cube, numbers))
print(cubes)
print("Using map and a lambda")
cubes = list(map(lambda x: x**3, numbers))
print(cubes)
print("Using list comprehension")
cubes = [x**3 for x in numbers]
print(cubes)
