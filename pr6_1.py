def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_prime(start, end):
    return list(filter(is_prime, range(start, end + 1)))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
prime_num = find_prime(start, end)
print(f"Prime numbers between {start} and {end}: {prime_num}")
