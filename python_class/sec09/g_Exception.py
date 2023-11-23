import traceback
import json
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
       ##############Data를 json형식으로
        data = {"timestamp": current_time, "error_message":error_message}

        filename = f"traceback_{current_time}.json"
        with open(filename, "w", newline="") as file:
             json.dump(data,file,indent=4)

        print(f" 정보 {filename}")
