#2진화 코드   encoding, decoding
#import sys -> sys.getdefaultencoding()
# 문자열 인코딩확인   , sys.getfilesystemencoding() 파일 인코딩 확인

import sys
class BTest:
    def b_wrtie(self):
        f = open("file_test02.txt",'wb')
        str ='대한민국 우리나라'
        f.write(bytes(str,'utf-8')) # 1byte 이내 코드값 변환   ASCII   ,  (확장형 코드 =  scan code , unicode)
        #f.write(str)
        f.close()

    def b_read(self):
        f= open("file_test02.txt","rb")
        while   True:
            s = f.read(1)
            if s ==b'':
                break
            print(s.hex(), s)
        f.close()
    def b_mread(self):
        with  open("file_test02.txt","rb")  as f :
            m =f.read().decode('utf-8')
            print(m)


if __name__ == '__main__':
    b1= BTest()  #기본 생성자를 호출하면서 객체를 생성한다.  __init__(self)
    #b1.b_wrtie()
    b1.b_read()
    b1.b_mread()
    print(sys.getdefaultencoding())
    print(sys.getfilesystemencoding())
    print(sys.gettrace())
