from random import random, randint

#1
randomlist = [random() for i in range(10)]
print(randomlist)

#2
randomlist_gt05 = list(filter(lambda x: x > 0.5, randomlist))
print(randomlist_gt05)

#3
# แบบ INT
accont_list = [int(''.join([str(randint(1,9)) for _ in range(8)])) for _ in range(5)] # Just Gen 5 acount number
print(accont_list)
accont_list_f4d = [x//10000 for x in accont_list]
print(accont_list_f4d)

# แบบ String
accont_list = [''.join([str(randint(1,9)) for _ in range(8)]) for _ in range(5)] # Just Gen 5 acount number
print(accont_list)
accont_list_f4d = [x[:4] for x in accont_list]
print(accont_list_f4d)

