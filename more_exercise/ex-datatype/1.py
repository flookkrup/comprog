hour = int(input("Enter hours : "))

day = hour // 24
minute = hour % 24 * 60


print(f"{day} Day(s) {minute} Minute(s).")