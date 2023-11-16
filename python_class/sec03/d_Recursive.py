#팩토리얼 계산,피보나치 수열 , 하노이탑
#수열 : 일반항, 유한,무한, 수열의 종류(나열된 원소의 정렬)
#수열 : 숫자나 기호의 나열이며 일정한 규칙이나 패턴에 따라 정렬되어 있는 것
def factorial(n):
    print(f'---------{n}')
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#피보나치 수열
def fibonacci(n):
    if n<= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    #print(factorial(5))
    res = fibonacci(10)
    print("피보나치 수열의 10번째 값 :" , res)