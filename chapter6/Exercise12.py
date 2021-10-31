def Combination(m, n):
    if m < n:
        return 0
    if m == n or n == 0:
        return 1
    return Combination(m - 1, n) + Combination(m - 1, n - 1)

in_m, in_n = map(int, input("Enter m n : ").split())
print(f"Combination({in_m}, {in_n}) = {Combination(in_m, in_n)}")