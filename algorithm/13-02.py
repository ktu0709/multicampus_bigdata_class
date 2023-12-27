'''
이진 검색
'''
import random
def binSearch(ary,data):  
    global count  
    pos = -1
    start = 0
    end = len(ary)-1
    middle = 0
    while(start <= end):
        count += 1
        middle = (start +end) // 2
        if(ary[middle] == data):
            pos = middle
            break
        elif(ary[middle] < data):
            start = middle + 1
        else:
            end = middle - 1
    return pos

dataary = [random.randint(0,9999999999)for _ in range(10000000)]
findata = random.choice(dataary)
dataary.sort()
print('정렬 끝')

count = 0
#print('배열 -->',dataary)
pos = binSearch(dataary,findata)
if(pos!=-1):
    print(findata,'는',pos,'위치에 있어요(',count,'번)')
else : 
    print(findata, '검색실패')