class AA:
    def my_method(self):
        print( "AA's my_method")


class BB:
    def my_method(self):
        print("BB's my_method")

class CC(AA,BB):
    def my_method(self):
        #super(AA, self).my_method()
        #super(BB, self).my_method()
        AA.my_method(self)
        BB.my_method(self)

if __name__ == '__main__':
    c  = CC()
    c.my_method()