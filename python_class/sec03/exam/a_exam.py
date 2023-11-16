def MyTest(a,b,c,d): #매개변수의 초기값이 없는 함수를 선언해서 호출할 경우 반드시 순서 및 변수명을 호출해서 값대입 호출
    print(a,b,c,d)


def MyTest02(a=10,b=2,c=0,d=0): #초기값이 있을 경우, 값전달 없이 호출 해도 된다
    print(a,b,c,d)

if __name__ == '__main__':
    MyTest(1,2,3,4)
    print('-----------------')
    MyTest02(c=77,d=23)
    print('-----------------')
    print(MyTest(1,2,3,4))