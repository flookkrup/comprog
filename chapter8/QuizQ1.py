# Function to check circularly identical
def isCircularlyIdentical(list1, list2):
    # Double list 1
    list1.extend(list1)
    
    # Traversal to double of list1
    for i in range(len(list1)):
        if list2 == list1[i : i + len(list2)]:
            return True
    
    # Finish traversal and no match
    return False

list1 = list(map(int, input("please input values in list1: ").split()))
list2 = list(map(int, input("please input values in list2: ").split()))

if isCircularlyIdentical(list1, list2):
    print("yes")
else:
    print("no")