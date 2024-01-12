class ClassWithGetSet:

    def __init__(self):
        self.__msg = 'hello world'
    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self,x):
        self.__msg = f'hello {x}'


class MyConstants:
    @staticmethod
    def foo(param):
        return f'foo {param}'

class MyConstants02:
    @staticmethod
    def foo(cls):
        return f'foo'


class Myclass:
    class_var = 10 #클래스변수
    @staticmethod
    def static_method(): #정적메소드 : 독립 수행
        print('정적메소드')
        
    
    @classmethod
    def class_method(cls): #cls = 클래스 자체를 의미
        print('클래스 메소드 호출,클래스 변수 호출 :',cls.class_var)


if __name__ == '__main__':
    instance = ClassWithGetSet()
    print(instance.msg)
    instance.msg = 'cake'
    print(instance.msg)

    print(MyConstants.foo("bar"))

    Myclass.static_method() #클래스와 독립적인 메소드를 정의해서 호출
    Myclass.class_method() #클래스의 상태와 상호작용하는 메소드를 정의해서 호출
    
    ### 인스턴스 변수는 각 객체 인스턴스에 고유한 데이터를 저장하는 반면
    ### 클래스 변수는 클래스의 모든 인스턴스 간에 공유되는 데이터를 저장한다

#########################

