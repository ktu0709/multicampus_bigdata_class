#파일의 임의 접근을 해보자

f=open("data.txt","r")
str  = f.read()  # 전체 파일의 내용을 읽어서 리턴
print(str)
print("=================================")
f.seek(0) #파일 포인터의  위치를  0으로 이동
while (1):
    l =f.readline() #한줄씩 읽어서 리턴
    if(l):
        print(l ) #출력을 한다.
    else:
        break

print("=================================")
f.seek(0)
print(f.tell())
print(f.read())
# ls= f.readlines()
# print(ls) #전체 출력
#
# #f.seek(0)
# print(ls[2][3], "\t",ls[8][10])
# print(f.tell())

#print("===============================")
#f.seek(20)
#print(f.read())
f.close()
print(type(f))


