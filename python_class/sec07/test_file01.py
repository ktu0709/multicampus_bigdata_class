str ='''mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).'''

f=open("data.txt",'w') #현재 패키지  sec07 하위에  data.txt 파일을 쓰기전용으로 생성 후 내용 저장
f.write(str)  # 'write', 'writelines'
f.close()

print(dir(f))

f=open("data.txt",'r')
print(f.read())  #'read', 'readline', 'readlines'
f.close()



