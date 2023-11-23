#int 클래스를 상속받아서 기능을 확장 하자.
class MyInt(int):
    #기능확장
    def is_even(self):
        return self % 2 == 0

    def is_odd(self):
        return self % 2  != 0

    def squard(self):
        return self ** 2

if __name__ == '__main__':
    '''
    int([x]) -> integer
    int(x, base=10) -> integer
    '''
    my_number  = MyInt(10)  #int(x, base=10) -> integer

    print(f" Is even? { my_number.is_even() }")
    print(f" Is odd? {my_number.is_odd()}")
    print(f" Squard  : {my_number.squard()}")


