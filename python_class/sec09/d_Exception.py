import sys

if __name__ == '__main__':
    try:
        res = 10 / 0
    except  ZeroDivisionError as ZDE:  #   class  ZeroDivisionError : def __init__(self, args = "'division by zero')
                                       #   def __repr__  (self):  return  self.args
        print(sys.exc_info()) # pvm 실행정보
        print( format(type(ZDE)))
        print(format(ZDE.args))
        print(format(ZDE))