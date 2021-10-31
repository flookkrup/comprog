from math import ceil, sqrt

def isPrime(num):
    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            return False
    return True

inp = int(input("Enter Integer : "))
print(f"Is {inp} prime? {isPrime(inp)}")
