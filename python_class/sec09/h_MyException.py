import sys
class MyException(Exception): #__init__(self,/,*args,**kwargs)
    pass

def raise_exception(err_mgs):
    raise MyException(err_mgs) #프로그램 중단
if __name__ == '__main__':
    try:
        raise_exception("My Error12345")
    except MyException as e:
        print(e.args)
        print("예외 유형 " , sys.exc_info()[0])
        print("예외 인스턴스 객체 ", sys.exc_info()[1])
        print("예외에 대한 traceback = stackframe ,호출내용  ", sys.exc_info()[2])
        print("예외  원래 traceback 예외 e와 연결하는 사용하는 내용")
        e.with_traceback(sys.exc_info()[2])

