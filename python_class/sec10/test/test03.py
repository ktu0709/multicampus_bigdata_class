import json


class my_jsonObject:
    def __init__(self, res):  # res  = My_s
        self.__dict__ = res
        #print(self.__dict__, res)  # 출력확인


if __name__ == '__main__':
    data= [{"id" : 1 , "product" : "Laptop" , "price" : 800},
           {"id" : 2 , "product" : "Mouse" , "price" : 20},
           {"id" : 3 , "product" : "Monitor" , "price" : 200}
          ]
    json.dump(data, fp=open("test03.json", "w"))

    f = open('test03.json', 'r')
    str = f.read()
    f.close()

    objdata = json.loads(str, object_hook=my_jsonObject)
    res = []
    for n in objdata:
        if n.price >= 50 :
            print(f'id : {n.id} , product : {n.product} , price : {n.price}')


'''
  with open('products.json', 'w') as file:
        json.dump(products, file)

    # 파일 읽기 및 필터링
    with open('products.json', 'r') as file:
        loaded_products = json.load(file)
    expensive_products = [product for product in loaded_products if product["price"] >= 50]

    # 필터링된 데이터 출력
    print("문제 3 결과:", expensive_products)
'''





