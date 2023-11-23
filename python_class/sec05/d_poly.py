# 자료형 확장 ,UI 확장, 속성정의 확장
class MyList(list):  #시퀀스 자료형 상속
    ##기능을 추가 및 확장
    def sum(self):
        return sum(self)
    def average(self):
        return sum(self) / len(self)


if __name__ == '__main__':
    my_list  = MyList([1,2,3,4,5])
    print(dir(my_list))
    print(my_list, type(my_list) )
    print (f'sum : {my_list.sum()}')
    print(f'avg : {my_list.average()}')
