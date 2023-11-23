#직렬화 , 역직렬화를 구현해 보자
import pickle

def case01():
    data  =[1,2,3,4,5]
    with  open("data.pkl", "wb") as file:
        pickle.dump(data,file)  #직렬화  [객체-> 바이트 스트림]

    with  open("data.pkl", "rb") as file:
        load_data  =pickle.load(file)
        print(load_data) #역직렬화  [바이트 스트림  -> 객체]

if __name__ == '__main__':
    case01()

