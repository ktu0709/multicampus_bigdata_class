#2진화 코드분 / byte(이미지,영상,네트워크 전송데이터) : bw , br
# ,   char  ->open /
# object (node) << 직렬화, 역직렬화    = stream
#임시기억장소 : 버퍼(1byte) , 클립보드(gui) ,누산기(가산기 안에 있는 연산데이터 프로세스) , 레지스터(명령어)
#stream : byte통로 (bit로 전환하여 전송)

class BTest:
    def b_wrtie(self):
        f = open("file_test01.txt",'wb') #바이너리로 파일에 쓰겠다
        f.write(b'ABC123') # 1byte 이내 코드값 변환   ASCII   ,  (확장형 코드 =  scan code , unicode 2byte= 0~ 65535)
        f.close()
    # 키보드 버퍼  ->   [버퍼링] stream (IO)   - > 파일
    def b_read(self):
        f= open("file_test01.txt","rb")
        while   True:
            s = f.read(1)
            if s ==b'':
                break
            print(s.hex(), s)
        f.close()

if __name__ == '__main__':
    b1= BTest()  #기본 생성자를 호출하면서 객체를 생성한다.  __init__(self)
    b1.b_wrtie()
    b1.b_read()
