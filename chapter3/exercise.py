# %%
# Exercise 1
w = float(input("น้ำหนัก = "))
h = float(input("สูง = "))

h /= 100

bmi = w / h ** 2

if bmi < 17.0:
    print("ผอมมาก")
elif bmi < 20.0:
    print("ผอม")
elif bmi < 25.0:
    print("ปกติ")
elif bmi < 40.0:
    print("อ้วน")
else:
    print("อ้วนมาก")

# %%
# Exercise 2
roomType = input("Enter room choice: ")

if roomType in ['D', 'd', 'G', 'g']:
    night = int(input("Enter nights to stay : "))
    
    if night > 0:
        if night <= 2:
            if(roomType == 'D' or roomType == 'd'):
                price = night * 3500
            elif(roomType == 'G' or roomType == 'g'):
                price = night * 4000
        else:
            if(roomType == 'D' or roomType == 'd'):
                price = night * 3000
            elif(roomType == 'G' or roomType == 'g'):
                price = night * 4000

        print(f"Payment is {price} baht")
    else:
        print("INVALID NIGHT")
else:
    print("INVALID CHOICE")

# %%
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
# %%
# Exercise 4
name, lastname = input("Enter name and lastname: ").split()
income = float(input("Enter income: "))
bonus = float(input("Enter bonus: "))

total = income + bonus

if total <= 150000:
    rate = 0
elif total <= 300000:
    rate = 5
elif total <= 500000:
    rate = 10
else:
    rate = 15

tax = total * rate / 100
print(f"Tax is {tax:.2f}")

# %%
