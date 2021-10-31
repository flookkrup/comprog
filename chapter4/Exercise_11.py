principle = float(input("Enter the principle : "))
interest_rate = float(input("Enter the interest rate : "))

year = 1

while year <= 5:
    interest = principle * interest_rate / 100
    balance = principle + interest
    
    print(f"year {year} Principle : {principle} , Interest : {interest} , Balance : {balance}")
    
    principle = balance
    year += 1