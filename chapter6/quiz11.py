def sum_digits (num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

inp = int(input("Enter Integer : "))
print(f"Sum digits : {sum_digits(inp)}")