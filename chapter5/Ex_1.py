result = 0.0

for i in range(1, 10):
    if i % 2 == 1:
        result += i / (i + 1)
    elif i % 2 == 0:
        result -= i / (i + 1)

print(f"Result : {result}")