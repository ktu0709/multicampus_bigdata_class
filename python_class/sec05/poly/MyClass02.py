#super() : 선조 클래스를 의미한다. 명시적으로 후손 클래스에서 선조의 변수나 메소드를 참조할때 사용한다.
#후손클래스에서 후손이 가진 값을 선조 클래스의 생성자를 호출해서 대입하려면 super()키워드를 사용한다.
from inspect import  *

class AA:
    def __init__(self):
        print("나 AA 생성자 ")

    def myDD(self):
        print(" -------------->  AA'myDD()")
class DD:
    def __init__(self):
        print("나 DD 생성자 ")
    def myDD(self):
        print(" -------------->  DD'myDD()")

class BB( AA ,DD  ):
    def __init__(self):
        AA.__init__(self) #선조의 기본 생성자를 호출
        DD.__init__(self)
        #AA.__init__(self)
        print("나 BB 생성자 ")
    def myDD(self):
        AA.myDD(self)
        BB.myDD(self )

if __name__ == '__main__':
    #a1 = AA()  #생성자를 호출하면서 객체가 생성되면 자유영역공간 메모리 할당된다.
    b1=BB()  # AA()  <- BB() 선조가 생성 된후  후손이 생성
    b1.myDD()

    print("3. 계층관계 : " , getmro(BB))