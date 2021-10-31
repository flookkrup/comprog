from math import pi

choice = int(input("Enter your choice (1,2,3) : "))
r = float(input("Enter radius : "))

if choice == 1:
    print(f"Area is {pi * r ** 2}")
elif choice == 2:
    print(f"Circumference is {2 * pi * r}")
elif choice == 3:
    print(f"Volume of Sphere is {4 / 3 * pi * r ** 3}")
else:
    print("Invalid choice")