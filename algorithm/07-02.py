def isQueueFull():
    global SIZE,queue,front,rear
    """
    if(rear>=SIZE-1):
        return True
    else:
        return False
    """
    #case 1 뒤가 그냥 빌때
    if(rear != SIZE-1):
        return False
    #case 2 : 진짜 꽉참
    elif(rear == SIZE-1 and front == -1):
        return True
    #case 3 : 앞에 여유 있을때
    elif(rear == SIZE-1 and front != 1):
        for i in range(front+1,SIZE,1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear  -= 1
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print('Queue is Full')
        return
    rear+=1
    queue[rear] = data

def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front ==rear):
        return True
    else:
        return False

def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print('Queue is Empty')
        return
    front +=1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print('Queue is Empty')
        return
    return queue[front+1]

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 1

enQueue('화사')
enQueue('솔라')
enQueue('문별')
print('출구<--',queue,'<--입구')

retData = deQueue()
print('손님 이리로 :',retData)
print('**준비하세요',peek())
print('출구<--',queue,'<--입구')

retData = deQueue()
print('손님 이리로 :',retData)

print('출구<--',queue,'<--입구')

enQueue('재남')
print('출구<--',queue,'<--입구')
