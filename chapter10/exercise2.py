data = "./table.csv"
table = {}

with open(data, "r") as file:
    next(file) # Skip header
    
    for line in file:
        course, credit, grade = line.strip().split(",")
        table[course] = {
            "credit": credit,
            "grade": grade
        }
    
    print(table)