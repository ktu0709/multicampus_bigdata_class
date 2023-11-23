import json


class my_jsonObject:
    def __init__(self, res):  # res  = My_s
        self.__dict__ = res
        #print(self.__dict__, res)  # 출력확인


if __name__ == '__main__':
    data= {"company" : "TechCorp",
           "employees" :[{"name" : "john Doe" , "department" : "HR" , "email" : "john@example.com"},
           {"name": "jane Smith", "department": "IT", "email": "jane@example.com"}]
           }
    json.dump(data, fp=open("test04.json", "w"))

    f = open('test04.json', 'r')
    str = f.read()
    f.close()

    objdata = json.loads(str, object_hook=my_jsonObject)
    for n in objdata.employees:
            print(f'name : {n.name} , department : {n.department} , email : {n.email}')


'''
   company_data = {
        "company": "TechCorp",
        "employees": [
            {"name": "John Doe", "department": "HR", "email": "john@example.com"},
            {"name": "Jane Smith", "department": "IT", "email": "jane@example.com"}
        ]
    }
    with open('company.json', 'w') as file:
        json.dump(company_data, file)

    # 파일 읽기 및 직원 정보 출력
    with open('company.json', 'r') as file:
        loaded_company_data = json.load(file)
        for employee in loaded_company_data["employees"]:
            print(f"문제 4 결과: {employee['name']} - {employee['email']}")
'''



