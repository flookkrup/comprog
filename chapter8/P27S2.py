def sum67(list):
    sum = 0
    toSum = True
    
    for i in list:
        # Check if find 6 turn toSum to False
        if i == 6:
            toSum = False
        if toSum:
            sum += i
        # Check if find 7 turn toSum back to True
        if not toSum and i == 7:
            toSum = True

    return sum

print(sum67([1,  2,  2])) #5 
print(sum67([1,  2,  2,  6,  99,  99,  7]))#5 
print(sum67([1,  1,  6,  7,  2]))#4 
print(sum67([1,  6,  2,  2,  7,  1,  6,  99,  99,  7])) #2 
print(sum67([1,  6,  2,  6,  2,  7,  1,  6,  99,  99,  7]))#2
print(sum67([2,  7,  6,  2,  6,  7,  2,  7])) #18 
print(sum67([2,  7,  6,  2,  6,  2,  7])) #9 
print(sum67([1,  6, 7, 7]))  #  8 
print(sum67([6, 7,  1,  6,  7,  7])) #  8 
print(sum67([6, 8,  1,  6,  7])) #  0 
print(sum67([]))  # 0
print(sum67([6, 7,  11]))  #  11 
print(sum67([11,  6,  7,  11]))  #  22 
print(sum67([2, 2,  6,  7, 7])) #  11
