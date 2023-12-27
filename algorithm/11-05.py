import random

def selectsort(ary):
    n=len(ary)
    for i in range(0,n-1) :
        minIdx=i
        for k in range(i+1,n):
            if(ary[minIdx]>ary[k]):
                minIdx = k
        ary[i],ary[minIdx] = ary[minIdx] , ary[i]
    return ary


dataary =[random.randint(33,190)for _ in range(10)]

print('정렬전 -->',dataary)
selectsort(dataary)
print('정렬후 -->',dataary)
