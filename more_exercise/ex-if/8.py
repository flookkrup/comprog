distance = float(input("Enter travel distance (km.) : "))
type_car = int(input("Enter type of car : "))
driving_pattern = int(input("Enter driving pattern : "))

if type_car == 1:
    if driving_pattern == 1:
        fuel = distance / 12
    elif driving_pattern == 2:
        fuel = distance / 10
elif type_car == 2:
    if driving_pattern == 1:
        fuel = distance / 10
    elif driving_pattern == 2:
        fuel = distance / 8
elif type_car == 3:
    if driving_pattern == 1:
        fuel = distance / 9
    elif driving_pattern == 2:
        fuel = distance / 7

print(f"Fuel required : {fuel:.2f} litres.")
