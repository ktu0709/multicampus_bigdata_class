from  dataclasses import *
class Calc:
    def __init__(self,a,b):
            self.a=a
            self.b=b

    def getHap(self):
        return self.a + self.b

    def getsub(self):
        return self.b-self.a

    def getMul(self):
        return self.a*self.b

    def getDiv(self):
        return self.b / self.a

    def __str__(self):
        return (f'====결과===== \n {self.a} + {self.b} = {self.getHap()}\n'
                +f' {self.b} - {self.a} = {self.getsub()}\n'
                +f' {self.a} * {self.b} = {self.getMul()}\n'
                +f' {self.b} / {self.a} = {self.getDiv()}')


C = make_dataclass('C',
                   ['a','b'],
                   namespace={'getHap': lambda self: self.a + self.b,
                              'getsub': lambda self: self.b + self.a,
                              'getMul': lambda self: self.a * self.b,
                              'getDiv': lambda self: self.b / self.a,
                              '__str__' : lambda self: f'====결과===== \n {self.a} + {self.b} = {self.getHap()}\n'
                                                      +f' {self.b} - {self.a} = {self.getsub()}\n'
                                                      +f' {self.a} * {self.b} = {self.getMul()}\n'
                                                      +f' {self.b} / {self.a} = {self.getDiv()}'})


if __name__ == '__main__':
        cm = Calc(100,200)
        print(cm)
        print()


        print('=======make_dataclass 메소드를 통해 Calc 클래스랑 똑같은 클래스 생성=====')
        c = C(100, 200)
        c.getHap()
        print(c)

        print(help(make_dataclass))
