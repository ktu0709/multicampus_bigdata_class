#-----------for문

#1)목록을 주면  요소**2 를 구한후  []로 리턴
def examfor():
    numbers=[1,2,3,4,5]
    squared_numbers =[lambda  x: x**2  for  x in numbers]
    #x의 제곱값을 계산하기 위한  func(x)로 numbers 현재 숫자 X로 호출
    res = [ test(x) for test,  x in zip( squared_numbers , numbers )  ]
    print(type(squared_numbers) , squared_numbers)
    print(res)

# examfor()에 대한 함수 변환
def examfor_func():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [x**2 for x in numbers]
    #res = [test(x) for test, x in zip(squared_numbers, numbers)]
    print(type(squared_numbers), squared_numbers)
    #print(res)


def examzip():
    name  =['a', 'e', 'i', 'o', 'u']
    age =  [1,2,3,4]
    tel = [11,22,33,44,55,66,77,88,99]
    zip_res  = zip(name,age,tel)
    print(zip_res)
    for  name, age, tel in zip_res:
        print(f'{name}  :{age}  : {tel}')



#2)문자열 목록을 대문자로 변환
def examfor02():
    strings = ["apple", "banana", "cherry"]
    uppercase_strings = [lambda s: s.upper() for s in strings]
    results = [q(s) for q, s in zip(uppercase_strings, strings)]
    print(results)

# examfor02()에 대한 함수 변환
def examfor02_func():
    strings = ["apple", "banana", "cherry"]
    uppercase_strings = [s.upper() for s in strings]
    #results = [f'q(s)' for q, s in zip(uppercase_strings, strings)]
    print(uppercase_strings)


#3) 목록에서 짝수를 필터링 하자.
def examfor03():
    numbers = [1, 2, 3, 4, 5]
    filtered_numbers = [lambda x: x for x in numbers if x % 2 != 0]
    results = [func(x) for func, x in zip(filtered_numbers, numbers)]
    print(results)

#examfor03()에 대한 함수 변환
def examfor03_func():
        numbers = [1, 2, 3, 4, 5]
        filtered_numbers = [ x for x in numbers if x % 2 != 0]
        print(filtered_numbers)


#4) 목록에서  하위 문자열 찾기
def examfor04():
    strings = ["apple", "banana", "cherry"]
    substring = "an"
    # 문자열 자체를 리턴하기 때문에  lambda s: s an포함 여부 상관없이 문자열만 리턴 된다.
    filtered_strings = [lambda s: s for s in strings if substring in s]
    results = [func(s) for func, s in zip(filtered_strings, strings)]
    print(results)

# examfor04()에 대한 함수 변환
def examfor04_func():
    strings = ["apple", "banana", "cherry"]
    substring = "an"
    filtered_strings = [s for s in strings if substring in s]
    print(filtered_strings)


def examfor04_res():
    strings = ["apple", "banana", "cherry"]
    substring = "an"
    filtered_strings = [s for s in strings if substring in s]
    results = filtered_strings
    print(results)



#5) 각 문자열에서 마지막 문자를 추출하자.
def examfor05():
    strings = ["apple", "banana", "cherry"]
    last_chars = [lambda s: s[-1] for s in strings]
    results = [func(s) for func, s in zip(last_chars, strings)]
    print(results)

# examfor05()에 대한 함수 변환
def examfor05_func():
    strings = ["apple", "banana", "cherry"]
    last_chars = [s[-1] for s in strings]
    print(last_chars)


#6) 각 단어의 첫글짜를 대문자로 표시하기
def examfor06():
    str ="process finished with exit code"
    res_words = [lambda w: w.capitalize() for w in str.split()]
    results = [func(w) for func, w in zip(res_words, str.split())]
    print(results)

# examfor06()에 대한 함수 변환
def examfor06_func():
        str = "process finished with exit code"
        res_words = [w.capitalize() for w in str.split()]
        print(res_words)


if __name__ == '__main__':
    examfor06()
    print('================')
    examfor06_func()




