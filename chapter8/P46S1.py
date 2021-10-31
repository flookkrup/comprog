mylist = [] 
mylist.append(5) 
mylist.insert(7,10) 
mylist.insert(0,3) 
mylist = mylist*2 
mylist = mylist+[2,4] 
mylist.remove(10) 
del mylist[0] 
mylist.sort() 
print(mylist)

# Result: [2, 3, 4, 5, 5, 10]