shopping_cart = {}
prices = {}

i = 1
while True:
    itemInfo = input(f"Enter item {i}: ")
    
    if itemInfo == "Done":
        break
    else: 
        item, quantity, price = itemInfo.split(",")
        quantity, price = int(quantity), float(price)
        
        if item in shopping_cart:
            shopping_cart[item] += quantity
        else:
            shopping_cart[item] = quantity
        
        prices[item] = price
        i += 1


checkout = {key: value * prices[key] for key, value in shopping_cart.items()}

print(f"You have to pay: {sum(checkout.values())}")
for item, price in checkout.items():
    print(f"{item}: {price:.1f}")