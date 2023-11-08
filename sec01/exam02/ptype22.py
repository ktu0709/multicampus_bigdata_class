y_value = [10, 20, 30, 40, 50]
# 새로운 리스트([60, 70]를 기존 리스트 s_value  뒤에 병합
y_value.extend([60, 70]) 
print (y_value)  #병합한 결과

# 주의: append로 새로운 리스트를 추가하면 하나의 리스트 요소로서 추가 
y_value.append([60, 70]) 
print (y_value)#추가된 결과

#다른 타입을 원하는 위치에 삽입 
y_value.insert(2, ( 'a' , 'b' ))
print (y_value)

