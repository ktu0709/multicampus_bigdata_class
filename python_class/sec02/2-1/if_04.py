
def If_test01() : #함수 안에 선언된 변수는 지역 변수
    score = int(input('input score: '))
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score < 90:
        grade = 'B'
    elif 70 <= score < 80:
        grade = 'C'
    elif 60 <= score < 70:
        grade = 'D'
    else:
        grade = 'F'
    print(grade)

def If_test02() :
    score = int(input('input score: '))
    if score>=90:
            grade = 'A'
    elif score<=89 and score>=80:
            grade = 'B'
    elif score<=79 and score>=70:
            grade = 'C'
    elif score<=69 and score>=60:
            grade = 'D'
    else:
        grade = 'F'
    print(grade)


def If_test03() :
    score = int(input('input score: '))
    grade = (
    'A' if 90 <= score <= 100 else
    'B' if 80 <= score < 90 else
    'C' if 70 <= score < 80 else
    'D' if 60 <= score < 70 else
    'F'
    )
    print(grade)

def If_test04():
    score = int(input('input score: '))
    grade = (
        'A' if score >= 90 else
        'B' if score >= 80 else
        'C' if score >= 70 else
        'D' if score >= 60 else
        'F'
    ) if 0 <= score <= 100 else 'Invalid score'
    print(grade)


if __name__ == '__main__':
    If_test04()
    pass
