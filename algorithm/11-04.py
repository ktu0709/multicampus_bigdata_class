import random

def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

before = [random.randint(33,190)for _ in range(8)]
after = []


print('정렬전 -->',before)

for i in range(len(before)) :
    minpos = findMinIndex(before)
    after.append(before[minpos])
    del(before[minpos])


print('정렬후 -->',after)
