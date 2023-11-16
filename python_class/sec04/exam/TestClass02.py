#이름 , 주소 , 전화 번호를 관리하는 Address 라는 클래스를 선언해서 변수로 값을 저장해 보자

class Address:
    name="Dominica"
    addr = "seoul"
    tel ="02-0000-000"

    def __init__(self):
        self.name = '00000000'
        self.addr = '00000000'
        self.tel = '00000000'

    def prn(self):  # 멤버 메소드
       print(Address.name, Address.addr, Address.tel) #클래스 변수로 호출(공용변수)

    def prn02(self):
        print(self.name, self.addr, self.tel) #객체(인스턴스 변수로 호출)

if __name__ == '__main__':
    print(Address.name, Address.addr, Address.tel)
    Address.name ="1111111111111"
    print(Address.name, Address.addr, Address.tel)
  #------------------생성된 객체  ----------------
    a1 = Address()
    a1.prn()

  #------------------생성된 객체  ----------------
    a2 = Address()
    a2.prn()

    print("============인스턴스변수와 메소드호출==================")
    a1.prn02()
    a2.prn02()