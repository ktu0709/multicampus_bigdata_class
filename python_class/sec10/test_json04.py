'''
홍길동 서울시 02-0000
박길동 부산시 051-0000
정길동 인천시 032-0000
'''

'''
1) 위 주소록 json으로 저장해 보자. 키를 name , addr , tel로 구현하자
2) 파일 이름은 address.json
3) 이름 : 홍길동 , 박길동 , 정길동
   전화번호 :
   주소    :
'''
import json

class my_jsonObject:
    def __init__(self, res):  #res  = My_s
        self.__dict__ = res
        print(self.__dict__, res) #출력확인


if __name__ == '__main__':
        address_data = [{"name" : "홍길동" , "addr" : "서울시" , "tel" : "02-0000"},
                        {"name": "박길동", "addr": "부산시", "tel": "051-0000"},
                        {"name": "정길동", "addr": "인천시", "tel": "032-0000"}
                        ]

        json.dump(address_data , fp = open("address.json","w"))
        file = open("address.json", 'r')  # r+b
        result = json.load(fp=file)
        #print(result)
        names = ', '.join(entry['name'] for entry in address_data)
        addrs = ', '.join(entry['addr'] for entry in address_data)
        tels = ', '.join(entry['tel'] for entry in address_data)
        print(f'이름: {names}')
        print(f'전화번호: {tels}')
        print(f'주소: {addrs}')
        file.close()
