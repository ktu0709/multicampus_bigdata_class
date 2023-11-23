import json
def Test01():
    data=[{'a':'A', 'b':(2,4), 'c':3.0}]  # list
    print('data :', data , 'repr(data) : ' ,repr(data), str(data))
    print(type(data) ,   type(repr(data)))
    data_string = json.dumps(data) #Serialize obj to a JSON formatted str 파이썬 데이터를 json형식으로 변환후 문자열로 리턴
    print('json :', data_string , type(data_string)) # 결과확인

def Test02():
    data ={'a': 'A', 'b': (2, 4), 'c': 3.0}  # {}
    data_string = json.dumps(data, indent=4,sort_keys=True) #인코딩
    print('Encoded :', data_string)
    #repr(data_string))
    decoded  = json.loads(data_string) #디코딩
    print("decoded :", decoded)  # type 확인

def Test03():
    obj_json = '{"str": [42.2], "str01": 42}'  #str
    obj = json.loads(obj_json)
    print(obj)
    print(json.dumps(obj, indent=4, sort_keys=True))

def Test04():
    obj_json = {"str": [42.2], "str01": 42,"str03": [42.2] ,"str02":'대한민국',}

    file  = "data.json"
    json.dump(obj_json,fp=open(file,'w'),indent=4, sort_keys=True)

    #파일에서 읽어서 화면 출력 하기
    file = open("data.json", 'r') #r+b
    result = json.load(fp=file )
    print(result)
    file.close()

if __name__ == '__main__':
    Test04()


