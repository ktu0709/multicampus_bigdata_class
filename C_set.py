a={1,4,5,6,10}
b={6,10,7,8,9}
print(a)
print(b)

print('=======합집합 :',(a|b), a.union(b))
print('=======차집합 :',(a-b), a.difference(b))
print('=======교집합 :',(a&b), a.intersection(b))
print('=======배타 집합 :',(a^b), a.symmetric_difference(b))
