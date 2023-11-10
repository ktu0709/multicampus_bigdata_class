s_value = [10, 20, 20,30, 40, 50]
print (s_value)

s_value.remove(10) # 자료 값 10 삭제
print (s_value)

#같은 자료 값이 여러개 존재하면 첫번째 것만 삭제
s_value.remove(20)
print(s_value)

#역순으로 리턴
s_value.reverse()
print(s_value)

#마지막에 있는 원소를  리턴. 
print(s_value.pop())

#길이를 리턴
print(len(s_value))