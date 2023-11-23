from sec04.exam02.MyCalc import Calc

if __name__ == '__main__':
     #c1 = Calc(100,50)
     #print(c1)

     mlist =[Calc(100,50),Calc(200,150),Calc(300,250)]
     list(map(lambda x : print(x),mlist))

     #a의 값이 100인값을 찾아서 777 바꾼 후 출력 하고
     print('=====a의 값이 100인값을 찾아서 777 바꾼 후 출력 하고======')
     '''
     def change(x):
          if x.a == 100:
               x.a = 777
          print(x)     
     list(map(lambda x: change(x) , mlist))
     '''

     m_list = list(map(lambda x: Calc(777, x.b) if x.a == 100 else x, mlist))
     list(map(lambda x: print(x), m_list))

     # b 값이 150인값을 찾아서 888  바꾼 후 출력 하자
     print('=====b 값이 150인값을 찾아서 888  바꾼 후 출력 하자======')
     y_list = list(map(lambda x: Calc(x.a,888) if x.b == 150 else x,mlist))
     list(map(lambda x: print(x), y_list))

