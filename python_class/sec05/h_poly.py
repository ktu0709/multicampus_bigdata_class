# 오브젝트 리스트
class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"MyClass(name='{self.name}')"

if __name__ == '__main__':
    '''
    obj1 = MyClass("Object 1")
    obj2 = MyClass("Object 2")
    obj3 = MyClass("Object 3")
    
    my_list = [obj1, obj2, obj3]
    '''
    my_list  =[MyClass("Object 1"), MyClass("Object 2"), MyClass("Object 3")  ]
    #만일 개체중 Object 1의 이름이 있다면 홍길동으로 변경하자.
    for obj in my_list:
        if obj.name == "Object 1":
            obj.name ='홍길동'
            print(f'find object :  {obj}')
        else:
            print(f'Other object :{obj}')

