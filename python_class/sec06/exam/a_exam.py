from abc import abstractmethod, ABCMeta

class AA(metaclass=ABCMeta):
    @abstractmethod #무조건 재정의 해라
    def prn(self): #생성 불가능
        print('AA')

class BB(AA):
    def prn(self):
        print('BB')

class DD(AA):
    def prn(self):
        print('DD')


def my_call(res : AA):
    res.prn()

def test(a : int): #데이터 타입을 명시하여 정적 바인딩
    pass

if __name__ == '__main__':
        #my_call(AA())
        my_call(BB())
        my_call(DD())