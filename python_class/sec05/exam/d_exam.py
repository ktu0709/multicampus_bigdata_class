#4) 상속관계를 통해서 후손을 통한 객체를 생성하고 후손의 객체를 통해서
# 메소드 호출, 재정의 개념을 통해 메소드 재정의를 구현해 보자

from inspect import  *

class AA:
    def prn(self):
        print("선조의 prn")

class BB(AA):
    def my_print(self):
        super().prn()
        print("후손의 prn")

class Myclass(BB):
    def prn(self):
        super().my_print()
        print("Myclass Prn")


if __name__ == '__main__':
    print("=====1. 후손을 통해 선조의 메소드를 호출해보자")

    a1 = Myclass()
    a1.prn()
    print("1. 클래스 객체 확인  :", isclass(Myclass))
    print("2. 매개인자 확인  :", getfullargspec(Myclass))
    print("3. 계층관계 : ", getmro(Myclass))
    print("4, 모듈확인  :", ismodule(Myclass))
    print("5. 멤버 확인  :", getmembers(Myclass))
    print("5. 소스 확인  :", getsource(Myclass))