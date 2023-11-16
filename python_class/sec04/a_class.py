'''
    a  b   ----Test
    선언 -> 객체생성 -> 멤버호춯 (값전달 및 변경 리턴)
    100 200
    300 400
    500 600
'''

#[1] 선언
class Test:
    #변수를 선언하고 초기화 하는 메소드(생성자) -> 객체를 생성할 때 단 한번만 호출된다./ 명시호출하지 않는다
    def __init__(self,a,b):
        self.a = a
        self.b = b

if __name__ == '__main__':
    #[2] 객체 생성
    t1 = Test(100,200)
    t2 = Test(300,400)
    t3 = Test(500,600)

    t1.a = 3000

    #[3] 멥버호출
    print(f'{t1.a} , {t1.b}')
    print(f'{t2.a} , {t2.b}')
    print(f'{t3.a} , {t3.b}')

    #각 stack 객체의 주소
    print("t1의 주소 : " ,id(t1))
    print("t2의 주소 : ", id(t2))
    print("t3의 주소 : ", id(t3))

    #각 heap 객체의 주소
    print("t1의 참조주소", t1) #Test 클래스는 __repr__ 없네....
    print("t2의 참조주소", t2)
    print("t3의 참조주소", t3)