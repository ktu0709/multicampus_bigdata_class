x = 10 # G에 해당
y = 11
print(id(x))
def foo():
    x = 20 # foo함수의 L에 해당, bar함수의 E에 해당
    print("foo's X=",x , id(x))
    def bar():
      a = 30 # L에 해당
      print( a, x, y ) # 각 변수는 L, E, G에 해당
    bar()
    x = 40
    bar()
def test():
    x= 2000
    print("test's X=", x, id(x))


if __name__ == '__main__':
    #foo()
    test()
    print('X=',x,id(x))
