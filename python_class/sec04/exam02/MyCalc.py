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


if __name__ == '__main__':
        cm = Calc(100,200)
        print(cm)
