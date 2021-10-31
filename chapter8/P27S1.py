def ForInListAverage(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

def ForInRangeAverage(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum / len(list)

list = [1, 2, 3, 4, 5]
print(ForInListAverage(list))
print(ForInRangeAverage(list))