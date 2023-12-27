import random

def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = i
    return ary[minIdx]


#testary = [55,88,33,77]
testary = [random.randint(33,190)for _ in range(10)]
minPos = findMinIndex(testary)
print('최솟값 : ',minPos)