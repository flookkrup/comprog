id = int(input("Enter id : "))

blacklist = [1, 7, 12]

while id > 0:
    if id not in blacklist:
        print(f"{id} got extra money")
    
    id = int(input("Enter id : "))