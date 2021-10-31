result = 0

for i in range(1, 11):
    if i % 2 == 0:
        result -= i
    elif i % 2 == 1:
        result += i

print(f"Result : {result}")