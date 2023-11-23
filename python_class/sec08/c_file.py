#seek() 위치를 찾는다
#tell()  현재 파일 위치
def case01():
    # test.txt 파일을 읽어서 seek()를 이용해서 efg를 읽어오자.
    with open("test.txt", "r") as file:
        file.seek(4)
        data = file.read(3)
        pos  = file.tell() #7
        print(data)
        file.seek(0)  #처음으로 보낸다.
        data02 = file.read(7)
        print(data02)
        pos02= file.tell() #현재 위치

    print(pos , pos02)

def case02(): # 데이터을 파일에서 읽어서 tell()을 사용해서 한줄씩 처리 후 번호를 출력해보자.
    with open('data.txt' ,'r') as file:
        line_number  = 1
        position  = file.tell()
        for line in file :
            print( f"line {line_number} :{ line.strip()}")
            line_number += 1
            #position = file.tell()
    #print(f"현재 파일의 위치 :{position}")

if __name__ == '__main__':
    case02()







