import sys
class NewException(Exception):
        pass

if __name__ == '__main__':
    try:
        a= int(input('input number : '))
        if a<0:
            raise NewException('0보다 작은디...') #raise는 생성될 클래스인 BaseException() 객체를 상속받은 클래스를 생성한다
    except NewException as e:
        print('------------------------',e,e.args)
        print(e.args)
        print("예외 유형 " , sys.exc_info()[0])
        print("예외 인스턴스 객체 ", sys.exc_info()[1])
        print("예외에 대한 traceback = stackframe ,호출내용  ", sys.exc_info()[2])
        print("예외  원래 traceback 예외 e와 연결하는 사용하는 내용")
        e.with_traceback(sys.exc_info()[2])