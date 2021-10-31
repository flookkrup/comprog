# list = [1,2,3,4,5]

# str = 'Hello'.join(map(str, list))
# print(str)

def circularly_identical(list1, list2):
    
    str1 = ' '.join(map(str, list2))
    str2 = ' '.join(map(str, list1 * 2))
    
    print(str1)
    print(str2)
     
    return str1 in str2
      
  
# driver code
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
  
  
# check for list 1 and list 2 
if (circularly_identical(list1, list2)):
    print("Yes")
else:
    print("No")

# check for list 2 and list 3 
if(circularly_identical(list2, list3)):
    print ("Yes") 
else:
    print ("No") 


