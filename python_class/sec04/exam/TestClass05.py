# 정수형 변수 a,b 를 관리하는 클래스를 만들어 보자. 단 캡슐화로 구현 해보자.
# 은닉된 멤버 변수에게  setxx으로 값 전달 및 변경하고   getxx return 메소드로 리턴하는 구조
class Test:
    def __init__(self) -> None:
        super().__init__()
        self.__a =0
        self.__b =100

    #__a=0  #주소  히든,  private 초기값은 생성자에서 대입
    #__b=0

    def setA(self, a): #지역변수 a
        self.__a =a  # 객체 생성후 값을 지역변수 a 로 전달받아  멤버__a 에게 값전달 및 변경
    def getA(self):
       return self.__a

    def setB(self,b):
        self.__b=b
    def getB(self):
        return self.__b

if __name__ == '__main__':
    t1 = Test()
    t1.setA(700)
    print(t1.getA())
    t1.setB(200)
    print(t1.getB())