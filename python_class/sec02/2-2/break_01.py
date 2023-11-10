def Test():
    for i in range(1,10):
            if i > 5:
                    break
            print("%5d"%i,end="")
    else:
        print("~else~")

    print(" outter = %5d"%i,end="")

def Test01():
    for i in range(1,10):
            if i > 3:
                    continue
            print("%5d"%i,end="")
            print("//")

    print(" outter = %5d"%i,end="")


def Test02():
    for i in range(1,10):
            if i > 5:
                    print(f"\n {i} > 5~~~",end=" ")
                    continue
            print("%5d"%i,end="")

    print(" outter = %5d"%i,end="")


if __name__ == '__main__':
    #Test01()
    Test02()
