'''
순차 검색
'''

import random
def seqSearch(ary,data):
    pos = -1
    for i in range(len(ary)):
        if(ary[i] == data):
            pos = i
            break
    return pos

dataary = [random.randint(33,190)for _ in range(10)]
findata = random.choice(dataary)

print('배열 -->',dataary)
pos = seqSearch(dataary,findata)
if(pos!=-1):
    print(findata,'는',pos,'위치에 있어요')
else : 
    print(findata, '검색실패')