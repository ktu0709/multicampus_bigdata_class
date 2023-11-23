#추상클래스  : abc.py  / dataclasses.py /  collections.abc
from abc import abstractmethod, ABCMeta
'''
 ***추상메소드를 가진 클래스는 추상클래스가 되고 객체 생성 불가능 <> 추상메소드가 없으면 추상클래스 생성 가능   
  1)선조가 가진 추상메소드를 후손이 재정의하지 않으면 객체를 생성할 수 없다
  2)재정의하지 않는 후손은 추상클래스를 된다.  
  
  Tip : 추상클래스란? 다형성과 동적 바인딩 (다양한 형태의 성질(기능)을 가진 후손클래스들을 추상 메소드로 통일하는 구조)
        -추상클래스 객체 생성 불가, 후손 추상메소드 반드시 재정의, 재정의 하지 않는 후손은 추상클래스가 된다
'''
#추상클래스
class Base(metaclass=ABCMeta) : # 난 객체 생성 안하는 추상클래스 . 단, 후손에게 강제로 추상메소드를 재정의 시킨다.

    #추상화 @을 함수위 에 지정할 수 있다.
    @abstractmethod   #추상메소드
    def start(self):
       pass
    @abstractmethod
    def stop(self):
        pass

class Cat(Base) :
    def start(self):
        print('Cat  start')
    def stop(self):
        print('Cat stop')


class Duck(Base) :
    def start(self):
        print('Duck  start')
    def stop(self):
        print('Duck stop')

class Puppy(Base):
    def start(self):
        print('Puppy  start')

    def stop(self):
        print('Pyppy stop')

def my_class(m : Base): #정적바인딩 타입 명시
     m.start()
     m.stop()


def my_class02(m):  #동적바인딩 타입 명시
    m.start()
    m.stop()


if __name__ == '__main__':
    my_class(Cat())
    #my_class02(Cat())
    my_class(Duck())
    my_class(Puppy())
    #my_class(Base())












