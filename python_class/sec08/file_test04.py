#파일의 임의 접근을 해보자
f=open("test.txt","r")
f.seek(3)
print(f.tell())
print(f.read(1))
print(f.tell())
print("===============================")
f.close()



