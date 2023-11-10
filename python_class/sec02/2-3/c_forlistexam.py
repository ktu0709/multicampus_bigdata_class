#홍길동남의 나이는 oo입니다 for,zip
def exam01():
    name=['홍길동','김수로','박혁거세','주몽']
    age=[21,22,23,24]
    for n,g in zip(name,age):
        print(f"{n}님의 나이는 {g}입니다")


#학생이름, 성적리스트, 주전공분야 -> dict 출력하자
def exam02():
    name=['홍길동','김수로','박혁거세','주몽']
    score=[70,52,63,94]
    majors = ['역사','국어','심리','수학']

    students_info = [{'Name' : n, 'Score' : s,'Majors':m} for n,s,m in zip(name,score,majors)]
    for elements in students_info:
        print(elements)

    #my answer
    for n,g,m in zip(name,score,majors):
        print(f"Name : {n} , Score : {g} , Majors : {m}")
    pass

def exam03():
    name=['홍길동','김수로','박혁거세','주몽']
    age=[21,22,23,24]
    res = [f'{name}님의 나이는 {age} 입니다.' for name , age in zip(name,age)]
    print(res)

#list를 사용하여 구구단 출력
def exam04():
            gugulist = [f'{i} x {j} = {i * j}'for i in range(2,10,2) for j in range(2,9,2)]
            print(gugulist)


if __name__ == '__main__':
    exam04()