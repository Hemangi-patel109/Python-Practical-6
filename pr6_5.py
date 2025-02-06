def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def fun(start, end):
    numbers = range(start, end + 1)
    results = map(lambda x: (x, square(x), cube(x)), numbers)
    return list(results)
start = 1
end = 5
output = fun(start, end)
print("Number, Square, Cube")
for num, sq, cu in output:
    print(f"{num}, {sq}, {cu}")
