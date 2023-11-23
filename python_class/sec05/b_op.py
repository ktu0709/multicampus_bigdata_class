class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return MyClass(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return MyClass(new_value)

if __name__ == '__main__':
    obj1 = MyClass(100)
    obj2 = MyClass(200)

    result = obj1 + obj2
    print(type(result))
    #final_result = result - MyClass(50)

    #print(final_result.value)
    # (MyClass(100) + MyClass(200) ) - MyClass(50)
