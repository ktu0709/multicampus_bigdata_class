import traceback
import csv
from datetime import datetime

def f1(a, b):
    return f2(a) + f2(b)

def f2(x):
    return 1.0 / x

if __name__ == '__main__':
    try:
        f1(1.0, 0.0)
    except (ZeroDivisionError, IOError):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H_%M_%S")  # Replace colons with underscores
        error_message = traceback.format_exc()

        data = [ [current_time, error_message] ]

        filename = f"traceback_{current_time}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print(f" 정보 {filename}")
        #csv 파일을 로드해서 화면에 출력 해보자.
