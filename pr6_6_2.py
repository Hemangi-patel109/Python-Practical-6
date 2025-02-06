#• Create a list of equivalent Celsius degree from Fahrenheit.

def to_celsius(f):
    return (f - 32) * 5/9
print("Using map and a function")
fahrenheit = [32, 68, 104, 122]
celsius = list(map(to_celsius, fahrenheit))
print(celsius)
print("Using map and a lambda")
fahrenheit = [32, 68, 104, 122]
celsius = list(map(lambda f: (f - 32) * 5/9, fahrenheit))
print(celsius)
print("Using list comprehension")
fahrenheit = [32, 68, 104, 122]
celsius = [(f - 32) * 5/9 for f in fahrenheit]
print(celsius)
