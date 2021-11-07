nLine = int(input("Enter n: "))
lines = {}

for i in range(1, nLine + 1):
    lineNumber, destination = input(f"Enter bus no. and destination {i}: ").split(", ")
    
    if destination in lines:
        lines[destination].append(lineNumber)
    else:
        lines[destination] = [lineNumber]

destination = input("Enter your destination: ")

if destination in lines:
    print(f"You can get bus no. {' '.join(lines[destination])}")
else:
    print(f"No buses go to {destination}")

