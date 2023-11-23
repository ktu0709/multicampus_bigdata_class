import sys


def  case01():
    try:
     res  = 10/0                  #ZDE = ZeroDivisionError('division by zero')
    except  ZeroDivisionError as  ZDE  : #pvm에서 Error의 종류에 해당하는 클래스를 생성해서 리턴되는 것을 except에서 해결한다
        print(" 0으로 나누려고 했잖아 예외처리 부분" , ZDE.args ,ZDE)
    else :
        print("else 예외가 나지 않을 경우 실행하는 부분")
    finally:
        print("오류 상관없이 반드시 수행할 명령  : 백업파일, 디비close() , 로그아웃  ")

    print( "===========case01============")

def case02():
    L= [1,2,3]
    try:
        num = L[4]
    except IndexError as IE:
        print("list index out of range" )  #  IndexError  : list index out of range
        print("IE =============> ",  IE , type(IE))
        #IE.with_traceback("abc") ##오류 실행
        tb = sys.exception().__traceback__
        print(tb , type(tb))
        num = L[0] #예외 처리
    else :
        print("else")
    finally:
        print("오류 상관없이 반드시 수행할 명령  : 백업파일, 디비close() , 로그아웃  ")
    print(num)



if __name__ == '__main__':
    case01()