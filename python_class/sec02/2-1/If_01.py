def If_test():
    my_id= input("Enter your id: ")
    if my_id == "a1234":  # 값 비교
        print("true : ",my_id)
        print("============")
        pass

def If_test02():
    my_id= input("Enter your id: ")
    if my_id != "a1234":  # 값 비교
        print("true : ",my_id)
        print("============")
        pass

def If_test03():
    if None:
        print("True")
    elif False:
        print("False")
    else:
        print("etc...")

if __name__ == '__main__':
    If_test03()

