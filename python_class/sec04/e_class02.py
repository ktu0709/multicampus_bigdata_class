# 클래스를 선언하게 되면 모든 클래스의 수퍼인 object의 자식이 되서 기능 및 변수등을 상속받게 된다
class Score(): #class에서 맴버는 self
    def __init__(my,name,kor,eng,mat): # -> None #객체를 생성할 때 값을 받으면서 생성하겠다.(초기값을 자동으로 생성하지 않고 받아서 초기화
        my.name = name
        my.kor  = kor
        my.eng  = eng
        my.mat  = mat

    def __repr__(my): #-> str
        return f'name = {my.name} , kor = {my.kor} , eng = {my.eng} , mat = {my.mat}'



if __name__ == '__main__':

   score_all =[Score('홍길동',90,80,70),
               Score('정길동', 50, 60, 70),
               Score('이길동', 100, 100, 100)
               ]
   print('=====================객체 배열 시퀀스형========================')
   for n in score_all:
       print(n)

   print('=====================언팩킹========================')
   print(*score_all)

   print('===================== map + lambda ========================')
   list(map(lambda x : print(x) , score_all))
