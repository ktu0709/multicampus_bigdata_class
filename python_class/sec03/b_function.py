#173
def prn(a=10 ,*res ,**mydict ):# (일반 데이터 변수,,,,*변수,**변수) -> 선언순서,단일변수
    "0000000000000000"
    print(a,"\t", res ,"\t", mydict)

if __name__ == '__main__':
     #선언  -> dir() -> help -> 사용법
     # 선언  -> dir() G확인  -> help 특성 -> 사용법,[내장속성=컴파일 속성값 ]
     # .py  -> .pyc  -> 컴파일 속성값
     prn(1,(2,[3,4],5,6), b=123, d=1, c=34, y=30)
     print(prn.__code__, type(prn.__code__))
     print(prn.__name__)
     print(prn.__defaults__)
     print(prn.__doc__)
     print(prn.__class__)
     res  = prn.__code__
     print(dir(res))
     print(type(prn))
     print(dir(prn))
