mystring = 'This String is contain number 12345 i love you 6789 i love you'

# 1
lenUpper = len([char for char in mystring if char.isupper()])
print(f"{lenUpper} upper case letters")

# 2
lenAlphaNumberic = len([char for char in mystring if char.isalnum()])
print(f"{lenAlphaNumberic} alpha numeric characters")

# 3
isContainIS = 'is' in mystring
print(f"'is' is in mystring {isContainIS}")

#4
onlyAlphaInEvenPosition = ''.join([char for char in mystring[::2] if char.isalpha()])
print(f"{onlyAlphaInEvenPosition}")

