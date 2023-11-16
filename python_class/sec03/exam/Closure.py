def quadratic( a, b, c ):
    cache = {}
    def f( x ):
        if x in cache:
            return cache[x]
        y = a * x * x + b * x + c
        cache[ x ] = y
        return y
    def mytest():
        return 999
    return f


if __name__ == '__main__':
    f1 = quadratic(3, -4, 5);
    print(f1)
    print(f1(0.1))
    #print(f1.__closure__)
    #print(type(f1.__closure__))
    #print(f1.__closure__[0])
    #f2 = quadratic(-2, 7, 10);
    #f2(0.4)
    res = [cell.cell_contents for cell in f1.__closure__]
    print(res)
    print(tuple(res))

