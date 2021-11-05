nBus = int(input("Enter n: "))
lines = {}

for i in range(1, nBus + 1):
    lineNumber, destination = map(str, input(f"Enter bus no. and destination {i}: ").split(", "))
    if destination in lines:
        lines[destination].append(lineNumber)
    else:
        lines[destination] = [lineNumber]

destination = input("Enter your destination: ")
print(f"You can get bus no. {' '.join(lines[destination])}")
