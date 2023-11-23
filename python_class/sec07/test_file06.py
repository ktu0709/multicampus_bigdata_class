#test_file03 ->  with문으로 수정한 클래스
class MyFile:
    def __init__(self, mypath, mystr):
        self.mypath = mypath
        self.mystr = mystr

    def my_write(self):
        with open(self.mypath, 'a') as f:
            f.write(self.mystr)

    def my_read(self):
        with open(self.mypath, 'r') as f:
            print(f.read())


if __name__ == '__main__':
    mypath = "data_test.txt"
    my_dict  = "{ 1:'a',2:'b',3:'c'}"
    m1 = MyFile(mypath,my_dict)  # 생성자 호출
    m1.my_write()
    m1.my_read()