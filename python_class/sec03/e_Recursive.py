def fibonacci(n):
    print(f'---------{n}')
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def recursive_sum(numbers):
    '''목록의 합  '''
    print(f'---------{numbers}')
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

def recursive_string(string):
    print(f'---------{string}')
    if len(string) <= 1:
        return string
    else:
        return recursive_string(string[1:]) + string[0]

if __name__ == '__main__':
    #print(fibonacci(5))
    numbers=[1,2,3,4,5,6,7,8,9,10]
    print(recursive_sum(numbers))

    print(recursive_string("ABCDEFGHIJKLMN"))