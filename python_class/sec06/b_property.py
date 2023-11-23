#####getter , setter : 값을 리턴하고, 값을 전달 및 변경하는 구조
class My:
    def __init__(self):
        self.x  =0
    @property
    def myFun(self):
        return  self.x #getter

    @myFun.setter
    def myFun(self, x):
         self.x =x  #setter
########################################################################

#클래스외부에서 함수를 선언하고
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1 #클래스 내부에서 참조하는 방법
    def g(self):
        return 'hello world'
    h = g

if __name__ == '__main__':
    c =C()
    y=c.g()
    print(y)
    r =c.f(3,4)
    print(r)

'''
if __name__ == '__main__':
    m = My()
    m.myFun = 100
    print(m.myFun)
'''