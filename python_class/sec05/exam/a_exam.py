class AA:
    def prn(self):
        print("선조의 prn")

class BB(AA):
    def my_print(self):
        print("후손의 prn")


if __name__ == '__main__':
    print("=====1. 후손을 통해 선조의 메소드를 호출해보자")

    a1 = BB()
    print(a1)
    a1.prn()
    a1.my_print() #후손의 객체를 통해서 선조의 메소드를 자유롭게 호출할수있다