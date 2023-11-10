'''
홀수인 경우:어떤 정수n에 대해서 n%2의 결과가 1이면 n은 홀수
홀수인 경우:어떤 정수n에 대해서 n%2의 결과가 0이면 n은 짝수
정수의 배수 : 어떤 정수n에 대해서, n% 배수의 결과 0일 경우 n%5 == 0

'''


def Test():
    for i in range(10):  #0 ~  9    range(stop)
            if i % 2 != 0:
                        continue
            print("%5d"%i,end="")  


def Test01():
    for i in range(102):  # 0 ~  9    range(stop)
        if i % 2 == 0:
            print("%5d" % i, end="")

def Test02():
    for i in range(1,102):  # 0 ~  9    range(stop)
        if i % 3 == 0 :
            print("%5d" % i, end="")

def Test03():
    for i in range(1,102):  # 0 ~  9    range(stop)
        if i % 2 == 0 and i % 3 == 0:
            print("%5d" % i, end="")

def Test04():
    count = 0
    for i in range(1,102):  # 0 ~  9    range(stop)
        if i % 2 == 0 and i % 5 == 0:
            print("%5d" % i, end="")
            count=count + 1
    print("\nCount : " ,count)

def Test05():
    count = []
    for i in range(1,102):  # 0 ~  9    range(stop)
        pass
        if i % 2 == 0 and i % 5 == 0:
           # print("%5d" % i, end="")
            count.append(i)
    else:
        print(f"count={len(count)},value={count}")


if __name__ == '__main__':
    functions = {'1':Test,
               '2': Test01,
               '3': Test02,
               '4': Test03,
               '5': Test04,
               '6': Test05
               }
    a = input("function : ")

    if a in functions:
        functions[a]()
    else:
        print("input error")

