def check_date(m, d, y):
    # Check if the date is valid
    if m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            if d > 29:
                return False
        elif d > 28:
            return False
    elif m in [4, 6, 9, 11]:
        if d > 30:
            return False
    elif d > 31:
        return False
    return True

in_d, in_m, in_y = map(int, input("Enter a date (dd/mm/yyyy): ").split('/'))

if check_date(in_m, in_d, in_y):
    print(f"{in_d:02d}/{in_m:02d}/{in_y} is Valid date")
else:
    print(f"{in_d:02d}/{in_m:02d}/{in_y} is Invalid date")