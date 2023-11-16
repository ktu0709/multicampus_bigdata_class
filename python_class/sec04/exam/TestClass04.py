# 캡슐화 : 은닉된 멤버 변수에 오픈된 메소드로 값을 전달(setXX)  및  변경하고  (getXX return) 리턴하는 구조
# getter & setter
class Test:
    __b=100 #객체 생성 후 호출할 수 없고, Test의 멤버만 접근 가능하다.
    __nic_name__ = 'Dominica' #강한 private이면서 의미있는 속성, 객체로 호출 가능하다
    _a =200 #약한 private -> 클래스 내부에서만 사용하자. 직접 접근하지 않았으면 좋겠다. 암묵적 지시 [호출은 가능하지만 ]
    def __m(self): #한문자를 리턴하는 private 메소드
        return 'a'
    def k(self):
        print(self.__m(), self.__b)


if __name__ == '__main__':
    my = Test()
    my.k()
    #print(my.__b)# 오류 ,,!!Test.__b X
    print(Test._a)
    #print(my._a)
