class MyClass:
    def __init__(self,name):
        self.name = name


    def __str__(self):
            return f'__str__ = {self.name}'


    def __repr__(self): #객체 정보 : 객체의 상태 또는 클래스이름, 메모리 주소를 리턴
        return f'__repr__ = {self.name}'


if __name__ == '__main__':
        obj = MyClass('oops')
        print(obj)
        print(str(obj))
        print(repr(obj))