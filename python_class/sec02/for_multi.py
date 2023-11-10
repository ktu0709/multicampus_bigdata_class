def Test01():
    for i in range(1, 4):
        print(f'={i}=')
        for j in range(1, 4):
            print(f"({i}, {j})", end=' ')
        print()

def Test02():
    start_num = 1
    matrix = ""
    for i in range(5):
        for j in range(5):
            matrix += f"{start_num}\t"
            start_num += 1
        matrix += "\n"
    print(matrix)

def Test03():
    for i in range(2, 10):
        print(f'=== {i} 단 ==')
        for j in range(1, 10):
            print ("%d * %d = \t" %(i, j), i*j)
        print(f'===========')

def Test04():
    start_num = 25
    matrix = ""
    for i in range(5):
        for j in range(5):
                matrix += f"{start_num}\t"
                start_num -= 1
        matrix += "\n"
    print(matrix)


#1번 숙제
def Test05():
    for i in range(5):
        rowdata = i + 1
        for j in range(5):
            print(f"{rowdata}", end=' ')
            rowdata = rowdata + 5
        print()

#2번 숙제
def Test06():
    for i in range(5):
        rowdata = 25 - i
        for j in range(5):
            print(f"{rowdata}", end=' ')
            rowdata = rowdata - 5
        print()

if __name__ == '__main__':
    Test06()
        
        
        
        