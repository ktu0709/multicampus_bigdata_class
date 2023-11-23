import json
My_s = '''
        {"name":"RuRi", 
        "brothers":["Ruse", "RuO"], 
        "addr":"Toronto"}
        '''

class my_jsonObject:
    def __init__(self, res):  #res  = My_s
        self.__dict__ = res
        print(self.__dict__, res) #출력확인

if __name__ == '__main__':
    # object_hook은 대상을 클래스인 객체로 연동해서 구현된다.
    data = json.loads(My_s, object_hook= my_jsonObject)
    print(data, type(data))
    print(data.name)
    print(data.addr)
    for brother in data.brothers:
        print(brother)