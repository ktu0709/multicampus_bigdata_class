def my(x,y,z):
    return x+y+z

def test01():
    #def my() : return 100
    res = lambda :100
    print(res, res())

def test02():
    '''
    def my(x):
    return 100+x
    '''
    res = lambda x :100+x
    print(res, res(10))

def test03():
    '''
    def my(x,y,z):
    return x+y+z
    '''
    res = lambda x,y,z:x+y+z
    print(res, res(1,2,3))

def test04():
    mylist=[1,2,3,4,5]
    res=lambda x:x
    print(res(mylist))

def test05():
    mylist=[1,2,3,4,5]
    res=lambda mylist : [x for x in mylist if x % 2 ==0]
    print(res(mylist))


if __name__ == '__main__':
    test05()