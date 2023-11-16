'''
name   kor  eng  mat    => Score
홍길동   90    80   70    => s1
정길동   50    60   70    => s2
이길동   100  100   100   => s3
'''

class Score:
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def getTot(self):
        return self.kor + self.eng + self.mat

    def getName(self):
        return self.name

    def setKor(self,kor):
        self.kor = kor

    def getAvg(self):
        return self.getTot()/3

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


if __name__ == '__main__':
    s1 = Score("홍길동", 90, 80, 70)
    s2 = Score("정길동", 50, 60, 70)
    s3 = Score("이길동", 100, 100, 100)

    print(f'{s1.name} {s1.kor} {s1.eng} {s1.mat} {s1.getTot()} {s1.getAvg()} {s1.getGrade()}')
    print(f'{s2.name} {s2.kor} {s2.eng} {s2.mat} {s2.getTot()} {s2.getAvg()} {s2.getGrade()}')
    print(f'{s3.name} {s3.kor} {s3.eng} {s3.mat} {s3.getTot()} {s3.getAvg()} {s3.getGrade()}')