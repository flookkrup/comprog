#%%
import math
x = 9
y = 5

print(y > 0 and math.sqrt(y) < x / y)

#%%
name = "Zoro"
print('A' <= name <= 'Z')

#%%
# Exercise 1
price = float(input("Enter price with vat: "))
vat = price * 7 / 107
print(f"Vat is {vat} Baht.")

#%%
# Exercise 2
from math import ceil
price = float(input("Enter price: "))
vat = ceil(price * 0.07)
print(f"Selling price is {price + vat : .0f} Baht")

# %%
# Exercise 3
from math import pi

radius, side = input("Enter radius and length of side: ").split()
radius, side = float(radius), float(side)

circleArea = pi * radius ** 2
squreArea = side ** 2

isLarger = circleArea > squreArea

print(f"This circle is larger than this square : {isLarger}")

# %%
name, months = input("Enter name and no. of months: ").split()
year = int(months) // 12
month = int(months) % 12
print(f"{name} has used this product for {year} year {month} month.")
