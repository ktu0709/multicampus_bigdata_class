''''
   1. com.test.MyScore :
       Score   : 이름 국어 영어  총점 평균 출력 메소드
       MyScore  :Score를 상속받아  5과목을 총 평균

    2. sec04.exam02.Score에서 호출을 해서 객체 배열을 만들어서 접근해 보자.
'''
from sec04.exam02.Score import *


class MyScore(Score):
    def __init__(self,name,kor,eng,mat,his,music):
        super().__init__(name,kor,eng,mat)
        self.his = his
        self.music=music

    def getTot(self):
        return super().getTot() + self.his +self.music

    def getAvg(self):
        return self.getTot() / 5

    def getGrade(self):
        avg = self.getAvg()
        return  avg
    '''
        if avg >= 90:
            return 'A'

        elif avg >= 80 and avg < 90:
            return 'B'

        elif avg >= 70 and avg < 80:
            return 'C'
        else:
            return 'F'
    '''

    def __str__(self):
        #return f'{self.name} {self.kor} {self.eng} {self.mat} {self.his} {self.music} {self.getTot()}  super :{super().getAvg()} self : {self.getAvg()} super : {super().getGrade()} self : {self.getGrade()}'
        return f'super Avg :{super().getAvg()} self Avg : {self.getAvg()} \nsuper GetGrade: {super().getGrade()} self GetGrade: {self.getGrade()}'


if __name__ == '__main__':
    s1 = MyScore("홍길동", 90, 80, 70,80,70)
    s2 = MyScore("정길동", 50, 60, 70,40,50)
    s3 = MyScore("이길동", 100, 100, 100,100,0)

    my_list = [MyScore("홍길동", 90, 80, 70,80,70),
               MyScore("정길동", 50, 60, 70, 40, 50),
               MyScore("이길동", 100, 100, 100, 100, 0)
               ]


    print(s1)
    #print(s2)
    #print(s3)

    #list(map(lambda x : print(x), my_list))