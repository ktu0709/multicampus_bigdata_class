#2개의 모든 조건이 맞을 경우 True : and , &
#조건중 1개만 맞아도 True : or , |
number = 1
if number <= 10 and number >= 1:
    print ("Great!")
else:
    print ("Wrong!")
    
if (number <= 10) & (number >= 1):
    print ("Great!222")
else:
    print ("Wrong!222")
