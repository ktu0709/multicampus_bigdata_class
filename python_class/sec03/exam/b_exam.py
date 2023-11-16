def myFunc(*a):
    print(a)

def myFunc01(*a,b=10):
    print(f'a={a} b={b}')

def myFunc02(*a,**d):
    print(f'a={a} d={d}')

def myFunc03(*a,b=10,**d):
    print(f'tuple={a} b= {b} dict={d}')

if __name__ == '__main__':
    #myFunc(1)
    #myFunc01(1)
    #myFunc02(1,2,3 ,d=1,y=200)
    mytuple = (1,2,3,4,5)
    mydict = {'a':1, 'b':2}
    '''
    myFunc02(mytuple,mydict)
    myFunc02(a=mytuple,d=mydict)
    myFunc02(*mytuple, **mydict)
    '''
    myFunc03(1,2,3,4 , z= 100 , y= 200)