from functools import reduce

def test01_map():
    number = [1,2,3,4,5]
    res = map(lambda x:x*2,number)
    print(list(res))

def test02_filter():
    number = [1,2,3,4,5]
    res = filter(lambda x:x%2==0,number)
    print(list(res))

def test03_reduce():
    number = [1, 2, 3, 4, 5]
    res = reduce(lambda x,y: x * y, number) #((((1*2)*3)*4)*5)
    print(res)


if __name__ == '__main__':
    test02_filter()

