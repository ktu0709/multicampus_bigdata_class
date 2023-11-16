import tkinter as tk
from MyCalc import Calc
#cm = Calc(100,200)
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        cm = Calc(num1, num2)
        operator = operator_var.get()

        if operator == '+':
            result = cm.getHap()
        elif operator == '-':
            result = cm.getsub()
        elif operator == '*':
            result = cm.getMul()
        elif operator == '/':
            result = cm.getDiv()
        else:
            result = "연산자 오류"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="값 오류")


# 윈도우 생성
window = tk.Tk()
window.title(" 나만의 계산기 ")
window.option_add('*Font', 'helvetica 14')

# Entry widgets으로 값 입력
entry1 = tk.Entry(window, width=10)
entry2 = tk.Entry(window, width=10)
#############라벨링
result_label = tk.Label(window, text="Result: ")
############### 라디오 버튼 연산자 선택
operator_var = tk.StringVar()
operator_var.set('+')
operator_frame = tk.Frame(window)
add_radio = tk.Radiobutton(operator_frame, text='+', variable=operator_var, value='+')
sub_radio = tk.Radiobutton(operator_frame, text='-', variable=operator_var, value='-')
mul_radio = tk.Radiobutton(operator_frame, text='*', variable=operator_var, value='*')
div_radio = tk.Radiobutton(operator_frame, text='/', variable=operator_var, value='/')

##############연산자 버튼
calculate_button = tk.Button(window, text="Calculate", command=calculate)

entry1.grid(row=0, column=0)
entry2.grid(row=0, column=1)
result_label.grid(row=1, column=0, columnspan=2)
operator_frame.grid(row=2, column=0, columnspan=2)
add_radio.grid(row=0, column=0)
sub_radio.grid(row=0, column=1)
mul_radio.grid(row=0, column=2)
div_radio.grid(row=0, column=3)
calculate_button.grid(row=3, column=0, columnspan=2)


window.mainloop()
