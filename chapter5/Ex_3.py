import os
file = os.path.expanduser('~/comprog/chapter5/file/grant.txt')

with open(file, 'r') as stdlist:
    both = 0
    tuition_c = 0
    expense_c = 0
    nogrant = 0
        
    TUITION_COST = 21000
    EXPENSE_COST = 8000
    
    for std in stdlist:
        std = std.strip()
        stdID, tuition, expense = std.split()
        
        if tuition == "Y" and expense == "Y":
            both += 1
        elif tuition == "Y":
            tuition_c += 1
        elif expense == "Y":
            expense_c += 1
        else:
            nogrant += 1
        
    budget = both * (TUITION_COST + EXPENSE_COST) + tuition_c * TUITION_COST + expense_c * EXPENSE_COST
    
    print(f"grant both : {both}")
    print(f"grant tuition fee : {tuition_c}")
    print(f"grant expense : {expense_c}")
    print(f"Not grant : {nogrant}")
    print(f"budger spent : {budget:,}")