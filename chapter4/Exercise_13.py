from math import sqrt

n = int(input())

isPrime = True

i = 2

while i <= sqrt(n):
    if n % i == 0:
        isPrime = False
        break
    i += 1
    
if isPrime:
    print(f'{n} is prime.')
else:
    print(f'{n} is not prime.')