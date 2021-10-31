x, y, z = input().split()
x, y, z = int(x), int(y), int(z)

isTrue = x ** 2 + y ** 2 == z ** 2

if isTrue:
    print("YES")
else:
    print("NO")