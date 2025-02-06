from functools import reduce

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
numbers = list(range(start, end + 1))
sum_of_range = reduce(lambda x, y: x + y, numbers)
print(f"The sum of numbers in the range {start} to {end} is: {sum_of_range}")
