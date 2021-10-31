import os

# These line just for MacOS
dirname = os.path.dirname(__file__)
filename = "./file/name.txt"

file = os.path.join(dirname, filename)

with open(file, 'r') as file:
    students = []
    for student in file:
        students.append(student.strip())
    
    wantToFind = input("Enter a name: ")
    
    if wantToFind in students:
        print("Student is in class")
    else:
        print("Student is NOT in class")
