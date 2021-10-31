n = int(input())

mx = n

while n >= 0 and n <= 100:
    n = int(input())
    mx = max(mx, n)

print(mx)