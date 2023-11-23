str ='''mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).'''

with open("data02.txt",'w')  as f:
    f.write(str)

print("=============read=========================")
with open("data02.txt",'r')  as f:
    print(f.read())

print("============readline()==========================")
with open("data02.txt",'r')  as f:
    print(f.readline())

print("=======readlines()===============================")
with open("data02.txt",'r')  as f:
    print(f.readlines())

print("================while readLine()======================")
f=open("data02.txt",'r');
while True:
    print(f.readline())




