import json
if __name__ == '__main__':
    data = {"name" : "john","age" : 30 ,"city" : "New York"}
    json.dump(data, fp=open("test01.json", "w"))

    file = open("test01.json", 'r')  # r+b
    result = json.load(fp=file)
    print(result)

    '''
        # 문제 1: JSON 데이터 읽기와 쓰기
        # 1단계: Python 딕셔너리 생성
        data1 = {"name": "John", "age": 30, "city": "New York"}

        # 2단계: 딕셔너리를 JSON 문자열로 변환하여 파일에 저장
        with open('data1.json', 'w') as file:
            json.dump(data1, file)

        # 3단계: 파일 읽기
        with open('data1.json', 'r') as file:
            loaded_data1 = json.load(file)

        # 4단계: 데이터 출력
        print("문제 1 결과:", loaded_data1)
    '''