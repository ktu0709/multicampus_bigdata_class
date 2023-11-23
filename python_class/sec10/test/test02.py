import json

class my_jsonObject:
    def __init__(self, res):  #res  = My_s
        self.__dict__ = res
        #print(self.__dict__, res) #출력확인


if __name__ == '__main__':
    data = {"employees" : [{"name":"john","age":30},{"name":"jane","age":25}]}

    with open('test02.json', 'w') as file:
        json.dump(data, file)

        # 파일 읽기 및 수정
    with open('test02.json', 'r') as file:
        loaded_data2 = json.load(file)
    loaded_data2["employees"][1]["age"] = 26  # Jane의 나이 수정

    # 수정된 데이터 저장
    with open('test02.json', 'w') as file:
        json.dump(loaded_data2, file)



