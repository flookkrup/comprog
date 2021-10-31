import os
file = os.path.expanduser('~/comprog/chapter5/file/bankbalance.txt')

"""

"""

with open(file, 'r') as statement:
    deposit = 0
    withdraw = 0    
    
    for transaction in statement:
        transaction = float(transaction.strip())
        if transaction > 0:
            deposit += transaction
        elif transaction < 0:
            withdraw += transaction
    
    print(f"Total Deposit : {deposit}")
    print(f"Total Withdraw : {abs(withdraw)}")
    print(f"Total : {deposit + withdraw}")