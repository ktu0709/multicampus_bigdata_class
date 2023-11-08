my_list=['cat','rat','dog','money']
print(my_list)

my_list[0]='puppy'     #my_list[0] 번지  값 수정
print(my_list)

del my_list[0]  #객체를 삭제 
print(my_list)

my_list.remove('rat') #요소삭제 
print(my_list)

my_list.append((10,20,30))#객체를 추가 (tuple)
print(my_list)

my_list.remove((10,20,30)) #값으로 삭제 
#del my_list[2]  #객체를 삭제 
print(my_list)