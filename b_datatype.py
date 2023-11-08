# 시퀀스->  리스트=CRUD , 터플CRUD(X) , str = 문자열= CRUD(X),  딕트 사전형
# 자료형 : 인덱스로 관리할 수 있다
items = ("apple", "banana", "cherry", "date")

print(items[0])#1. 튜플의 첫 번째 요소를 출력
print(items[-1])#2. 튜플의 마지막 요소를 출력
print(items.index("banana"))#3. 튜플에서 "banana"가 몇 번째 인덱스에 있는지 찾아 출력


############################################
# dict   {키 : 값 , ,,,}
fruits = {'apple': 2.5, 'banana': 1.2, 'orange': 1.0, 'grape': 3.0}

print(fruits.get('banana'))#1 fruits에서 'banana'의 가격을 출력
print(fruits.get('orange'))#2.orange'의 가격을 출력
print(fruits.get('apple') + fruits.get('grape'))#3.apple'과 'grape'의 가격을 더한 결과를 출력
fruits['watermelon'] = 4.5 #4.'watermelon'을 키로 가진 항목을 추가하고, 해당 키에 4.5 값을 할당
print(fruits)
fruits.update({'banana':1.5}) #5.'banana'의 가격을 1.5로 업데이트 코드 작성 후 출력
print(fruits)



