def  my_write():
    with open("data.txt","w") as f:
        for i in range(1,10):
            str  = "%3d  * %3d = %3d \n "% (2,i,2*i)
            f.write(str)

def my_read():
    with open("data.txt","r") as f:
        print(f.read())

if __name__ == '__main__':
    my_write()
    my_read()