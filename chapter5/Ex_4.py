import os
file = os.path.expanduser('~/comprog/chapter5/file/grant2.txt')

with open(file, 'r') as stdlist:
    both = 0
    tuition_c = 0
    expense_c = 0
    nogrant = 0
    
    budget = 0
    
    for std in stdlist:
        std = std.strip()
        stdID, tuition, expense = std.split(",")
        
        tuition, expense = float(tuition), float(expense)
        
        if tuition > 0 and expense > 0:
            both += 1
            budget += tuition + expense
        elif tuition > 0:
            tuition_c += 1
            budget += tuition
        elif expense > 0:
            expense_c += 1
            budget += expense
        else:
            nogrant += 1
    
    print(f"grant both : {both}")
    print(f"grant tuition fee : {tuition_c}")
    print(f"grant expense : {expense_c}")
    print(f"Not grant : {nogrant}")
    print(f"budger spent : {budget:,}")