"""
Condition :
    - "C" at least 1 letter
    - number 1 only once
"""

password = input("Please enter the password you want to check forvalidity: ")

if "c" in password and password.count("1") == 1:
    print("The password is valid")
else:
    print("The password is invalid")
