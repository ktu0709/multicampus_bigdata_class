import traceback
from datetime import datetime
def f1(a, b):
    return f2(a) + f2(b)

def f2(x):
    return 1.0 / x

if __name__ == '__main__':
    try:
        f1(1.0, 0.0)
    except (ZeroDivisionError, IOError):
        now = datetime.now() # 현재 시간 객체 생성 now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S") #포맷 패턴을 생성
        error_message = traceback.format_exc() # # 에라의 정보를 문자열로 리턴 받는다.

        filename = f"traceback_{current_time}.txt"  #파일이름 병합
        with open(filename, "w") as file:
            file.write(error_message)   #에라메시지 출력

        print(f"Traceback  저장 정보  {filename}") #파일명 확인
