#class  코드를 변환해 보자.
class MyFIle:
    def __init__(self,mypath,str ):
        self.mypath = mypath
        self.str = str

    def My_write(self):
        f=open(self.mypath,'a')  # 추가
        f.write(self.str)
        f.close()

    def My_read(self):
        f=open(self.mypath,'r')
        print(f.read())
        f.close()
if __name__ == '__main__':
    str = '''mode is an optional string that specifies the mode in which the file
        is opened. It defaults to 'r' which means open for reading in text
        mode.  Other common values are 'w' for writing (truncating the file if
        it already exists), 'x' for creating and writing to a new file, and
        'a' for appending (which on some Unix systems, means that all writes
        append to the end of the file regardless of the current seek position).'''
    mypath = "c:\\test\\data.txt"

    m1 = MyFIle(mypath, str) #생성자 호출
    m1.My_write()
    m1.My_read()

