def highest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

in_a, in_b, in_c = map(int, input("Enter three numbers: ").split())
print(f"Highest number is : {highest(in_a, in_b, in_c)}")