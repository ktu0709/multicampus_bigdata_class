class MyException(Exception):
    pass

def myPrn(a,b):
    if b== 0:
        raise MyException("0 이 잖아")
    return a/b

if __name__ == '__main__':
    try:
        res  =  myPrn(10,0)
        print(res)
    except MyException as e:
        print("Error  :", str(e))
        res = myPrn(10,100)
    finally:
        print(res)