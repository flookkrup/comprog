n = int(input("Enter n : "))

result = 0
i = n

while i > 0:
    result += i
    i -= 1

print(f"Fibonacci({n}) = {result}")