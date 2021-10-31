status = input("Enter status : ")
pay = float(input("Enter monthly pay : "))

if status.upper == "S":
    TAX = 0.2
else:
    TAX = 0.14

print(f"Tax : {pay*TAX:.2f}")