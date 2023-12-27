def isStackFull():
    global SIZE , stack , top
    if(top >= SIZE-1):
        return True
    else :
        return False

def push(data):
    global SIZE , stack , top
    if(isStackFull() == True):
        print('Stack Over')
        return
    top += 1
    stack[top] = data

def isStackEmpyt():
    global SIZE , stack , top
    if(top == 1):
        return True
    else:
        return False

def pop():
    global SIZE , stack , top
    if(isStackEmpyt()):
        print('No Stack data')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


SIZE = 5
stack= [None for _ in range(SIZE)]
top = -1

push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')
print('바닥',stack)

push('게토레이')
print('바닥',stack)

retdata = pop()
print('팝 -->',retdata)
print('바닥',stack)