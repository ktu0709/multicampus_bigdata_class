'''
이름    주소  전화번호
홍길동   서울   02-0000
정길동   인천    031-0000
최길동   나주    063-0000
'''

class Address:
    def __init__(self,name,addr,tel):
        self.name=name
        self.addr=addr
        self.tel=tel

    def __repr__(self):
        return f'이름 : {self.name} , 주소 : {self.addr} , 전화번호 : {self.tel}'


if __name__ == '__main__':
    address_all=[Address('홍길동','서울','02-0000'),
                 Address('정길동', '인천', '031-0000'),
                 Address('최길동', '나주', '063-0000')]
    print("1.전체 출력")
    list(map(lambda a : print(a),address_all))

    print("2.주소록 에서 홍길동의 이름을 찾아서 주소를 광주로 변형 후 전체 출력   ")

    for res in address_all:
        if res.name =='홍길동':
            res.addr = '광주'
    list(map(lambda a: print(a), address_all))

    print("=======[홍길동 레코드만 추출 map]======")
    list(map(lambda a: print(a) if a.name =='홍길동' else None, address_all))

    '''
    def update(x):
        if x.name=="홍길동":
            x.addr ='광주'
        print(x)
        return x

    list(map(lambda a : update(a),address_all))
    '''

    print("=======[홍길동 레코드만 추출 filter]======")
    def find_filter(x):
        if x.name =='홍길동':
            return True
        return False

    res=list(filter(lambda x : find_filter(x), address_all))
    res02 =list(filter(lambda x: (print(x),True) if x.name == '홍길동' else (None , False) , address_all))
    print(res)


    print("3.주소록 에서 정길동의 전화번호를  77777 변형 후 전체 출력   ")
    def update_03(x):
        if x.name == '정길동':
            x.tel = '77777'
        print(x)
    list(map(lambda a : update_03(a),address_all))


    print("4.최길동의 이름을 박길동 변형 후 전체 출력   ")
    def update_04(x):
        if x.name == '최길동':
            x.name = '박길동'
        print(x)

    list(map(lambda a : update_04(a),address_all))

    print("5.주소록 에서 홍길동의 전화번호를 02-8888 전체출력     ")
    def update_05(x):
        if x.name =='홍길동':
            x.tel='02-8888'
        print(x)

    list(map(lambda b : update_05(b),address_all))


    print("6.주소록 에서 정길동의  주소는 '제주도' 전화번호를 064 -0000 변경 후 전체 출력    ")
    def update_06(x):
        if x.name =='정길동':
            x.tel='02-8888'
            x.addr='제주도'
        print(x)

    list(map(lambda b : update_06(b),address_all))