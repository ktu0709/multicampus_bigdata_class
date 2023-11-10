#print("출력서식")  -> page 40 
import datetime  # 날짜 시간 모듈
import math
def case01():
    #정수, 실수, 문자열 각 10자리씩 출력해보자.    
    print("%10d %5d"%(100 , 200) )  #전체 정수 10자리 확보 후 100을 출력 , 5자리 확보후 200  
    print("%-5d %5d %5.1f"%(1,2,3.88888)) # 1 :정수5자리 왼쪽부터정렬 , 2 : 정수5자리 , 3.8888: 정수5자리 + 소수점1자리까지
    print("%10s : %10s "%("aaaaaa","bbbbbbbbbbbbbbbbbbb"))
    ##  정수, 8진수, 16진수  
    print("%d %o %x %5f"%(100,100,100,3.14)) #소수점 기본정밀도 자리가 출력

def case02():
    #str's format ->  S.format(*args, **kwargs) -> str
     print("{0} {1}".format( "apple", 7.77 ) )
     print("{1} {0}".format( "apple", 7.77 ) )
     print("{0} {0}".format( "apple", 7.77 ) )
     print("{0:^10s} {1:10f}".format( "apple", 7.77 ) )
     print("{1}/{1}/{1}".format("apple", 7.77))
 
def case03():
    #str.format() 정수활용해 보자 . 
    num =42
    num01 = 100
    f= "The number is {} {}".format(num,num01)
    print(f)

def case04():
    #str.format() 실수활용해 보자 . 
    pi=3.14159
    f= "The number is {: .2f} {}".format(pi,math.pi)
    print(f)
    
def case05():
    #str.format() 제로패딩 활용해 보자 . -> 수치 데이터 -> 저장대상 -> 0으로 채워서 저장 하고 싶을 때
    # 2진화 ,bin(value) -> int(bin(value),base=0)
    num =42
    f= "The number is {:010d}".format(num)
    print(f)
    f= "Binary is {:08b}".format(num)
    print(f)
    
def case06():  
    #날짜서식 date(year, month, day) --> date object
    date  = datetime.date(2023,7,7)
    f= "Date : {: %Y-%m-%d}".format(date)
    print(f)
    print("today:",datetime.datetime.today())
    print("today2:", datetime.datetime.now())
    print("today is : {: %Y-%m-%d}".format(datetime.datetime.today()))
    '''
    datetime 모듈에 datetime클래스의 today 함수와 now함수(각국가별 시간)는 timezone에 따라 달라진디
    1.datetime.datetime.today() : 로컬시간
    2.datetime.datetime.now()   : 컴퓨터시간
    '''
def case07():
    #튜플 -> * 
    point=(1,2,3,4)
    point01=(11,2,3,4)
    f= "Point: (  {},{},{},{}.{},{},{},{} )".format(*point,*point01)
    print(f)
    a,b,*c= 1,2,3,4,5,6,7
    print(a,b,c,type(c))

def case08():
    #사전형dict **  
    person={'name':'홍길동' ,'age77':20 , 'test':'test'}
    f="person : Name:{name} , age:{age77} , test:{test}".format(**person)
    print(f)
    

def case09():
    #인수위치  
    f=" {0} {1} {2}" .format(1,2,3)
    print(f)

if __name__ == '__main__':
    #case01()
    #case02()
    #case03()
    #case04()
    #case05()
    #case06()
    #case07()
    #case08()
    case09()




