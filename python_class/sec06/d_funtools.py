from functools import  singledispatch   # 함수의 오버로딩을 만드는데 사용하는 것

@singledispatch
def  my_data(data) :
    print("Error")

@my_data.register
def _(data :int, t :int):
    print(" int  " , data , t)
@my_data.register
def _(data :str):
    print(" str  " , data)
@my_data.register
def _(data:list):
    print("list" , data)

if __name__ == '__main__':
      my_data(10 ,100)
      my_data("abc")
      my_data([1,2,3,])
      my_data(90.9)
