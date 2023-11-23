#3) 상속관계를 통해서 후손을 통한 객체를 생성하고 후손의 객체를 통해서 [생성자 구문을 확인하고]
# 선조으 메소드와 후손의 메소드를 자유롭게 호출할 수 있다.
# 생성자를 통해 값전달을 해보자 선조(a)
class AA:
    def __init__(self,a,b):
        self.a = a
        self.b=b

    def prn(self):
        print("선조의 prn")

class BB(AA):
    def __init__(self,a,b): #2. 지역변수가 a=100 , b=200을 받는다
        super().__init__(a,b) #3. 선조으 생성자에서 100,200을 a,b라는 변수를 통해 전달한다

    def my_print(self):
        print("후손의 prn a",self.a)
        print("후손의 prn b", self.b)



if __name__ == '__main__':
    print("=====1. 후손을 통해서 선조의 메소드를 호출해보자")
    a1 = BB(100,200) #1. 후손 클래스의 생성자로 값을 전달
    a1.prn() #상속된 메소드 호출
    a1.my_print() #후손의 메소드 호출
