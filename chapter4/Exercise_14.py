start = 1
end = 20

factorial = [1]

while start <= end:
    factorial.append(start * factorial[start - 1])
    
    print(f"{start:2d}! = {factorial[start]}")
    start += 1
