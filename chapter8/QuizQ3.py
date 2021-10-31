sum = 0

transaction = input("Specify deposit and withdrawal amounts: ").split()

for i in range(0, len(transaction), 2):
    if transaction[i] == "D":
        sum += int(transaction[i+1])
    elif transaction[i] == "W":
        sum -= int(transaction[i+1])

print(f"Total amount is {sum}")


# D 300 D 300 W 200 D 300