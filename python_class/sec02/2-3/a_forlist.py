'''
  list  객체를  for문을 활용해서 연산결과를 list로 리턴 
  형식
  [ 리턴값  for  변수,, in list객체 ]   -> return 키워드가 없다. 
  List Comprehension '''
list1  =[1,2,3,4,5]

print( '1. 요소*요소 =>',[  x*x  for x in list1    ])

print( '2.(요소, 요소*요소) =>',[(x, x*x)  for x in list1    ])

print( '3. 요소*요소   짝수=>',[  x*x  for x in list1  if x % 2 == 0    ])

print( '4. 요소*요소 =>',[  x*x  for x in range(1,6)    ])

my_word  = ['apple','watermelon','peach','pear'] 
print( '5. 문자열을 대문자로 변환  =>',[  word.upper()  for word in my_word   ])

n_list= [[1,2,3 ],
         [4,5,6],
         [7,8,9]]
 #sublist  [1,2,3 ][4,5,6][7,8,9]
res_list  =  [ num for sublist in n_list
                   for num in sublist]
print('6. 중첩 연산  :' ,res_list)

# [ 표현식 for 항목 in iterable if 조건]
numbers = range(1,11)
print( '7. 1~ 10까지  even, odd  =>',['even' if x % 2 == 0 else 'odd' for x in numbers])


numbers = [1, 2, 7, 4, 5]
all_positive = all(x > 0 for x in numbers)  # data and data and None and....
print('8번 : ',all_positive )


is_even_res  = any( num % 2==0 for num in  numbers  )
print ('9번',is_even_res )


