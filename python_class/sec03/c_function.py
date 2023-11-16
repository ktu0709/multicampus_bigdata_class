from functools import partial #부분함수 , 함수분할

#함수의 원본
def power(base, exponent):
    return base ** exponent

#함수의 원본
def multiply(a, b):
    return a * b

if __name__ == '__main__':
              #partial(func, *args, **keywords)
    square = partial(power, base=2) #square 함수가 생성된다.
    print(square )
    result = square(exponent=3)
    print(result)
    #------------------------------------------#
    my_partial  =partial(multiply,5)   #부분함수 생성 a= 5
    result  = my_partial(3)  # b= 3 #원래 함수를 호출하게 된다.
    print(result)
