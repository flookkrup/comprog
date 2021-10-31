# Exercise 3
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month == 2:
    # Leap year check
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Number of days : 29")
    else:
        print("Number of days : 28")
    
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("Number of days : 31")
else:
    print("Number of days : 30")