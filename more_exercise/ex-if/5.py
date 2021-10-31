firstNumber = int(input("Enter first number: "))
operator = input("Enter operator: ")
secondNumber = int(input("Enter second number: "))

if operator == "+":
	print(firstNumber + secondNumber)
elif operator == "-":
	print(firstNumber - secondNumber)
elif operator == "*":
	print(firstNumber * secondNumber)
elif operator == "/":
	print(firstNumber / secondNumber)
else:
	print("Invalid operator") 
