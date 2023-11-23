import inspect #함수의 소스 코드와 인수를 출력 해보고 싶다.
'''
    모듈, 클래스 메소드, 함수등 라이브러리 객체를 검사하고 
    정보를 검색하기 위한 함수들로 되어있다.  
    코드검색, 호출가능 객체 , 인수목록, 상속계층등을 확인 
'''
def my_function(arg1, arg2):
    ''' this is  my_function 's  sample  '''
    print (arg1 + arg2)

if __name__ == '__main__':
        print(dir(inspect))
        source_code  = inspect.getsource(my_function)
        print(source_code)
        args =  inspect.getfullargspec(my_function)  # > help(inspect.getargspec) getargspec
        print(args)
        print(inspect.isfunction(my_function))



