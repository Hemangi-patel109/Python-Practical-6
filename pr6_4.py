def is_arm(number):
    digits = list(map(int, str(number)))  
    num_digits = len(digits)  
    return number == sum(map(lambda x: x ** num_digits, digits))
def arm_num(start, end):
    numbers = range(start, end + 1)
    return list(filter(lambda num: is_arm(num), numbers))
start = 100
end = 999
armstrong_numbers = arm_num(start, end)
print(f"Armstrong numbers in the range {start} to {end}: {armstrong_numbers}")

