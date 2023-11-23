#__str__ : 객체를 호출할 때 호출되는 자동 메소드    / __repr__
#object.__str__  => 객체클래스이름 , 주소 리턴하는 기능
#object.__repr__ -> 멤버 또는 출력하고 싶은 서식 사용자 서식 변환해서 리턴
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age  = age


    def __repr__(self):
        return f'Person(name ={self.name} , {self.age } )'

    def __str__(self):
        return f'Person(name ={self.name} , {self.age } )'

if __name__ == '__main__':
    p1  = Person("홍길동" ,30)
    print(p1)
    print(p1.__repr__)
    print(p1.__repr__())
    print(p1.__str__)


# __getattr __  :  값을 검증을 하고 싶을 때 재정의 즉 유효성 검사용
# 제어문 , [사용자 예외 클래스 생성 , 사용자 Error 클래스 정의로 제어  ]