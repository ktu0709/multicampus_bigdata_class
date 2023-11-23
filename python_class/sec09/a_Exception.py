#예외가 발생되면 pvm 예외 종류를 확인하고 확인된 객체를 생성해서
# 개발자는 예외발생한 위치를 확인하고 try ~ except 구문을 작성한다
# except 구문에서 예외를 처리한다

if __name__ == '__main__':
    a= 10
    b = 0
    res = 0
    try:
        res  = a/ b
        print('여기 이제 안된다')

    except ZeroDivisionError as zd:
        ### 예외 처리하는 부분
        print(type(zd))
        print(f'{a} / {b} = {res}')

    print('여기는 된다')