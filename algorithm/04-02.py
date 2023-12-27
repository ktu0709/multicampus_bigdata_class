## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, pre, current
    # Case1 : 찾는애가 헤드(=헤드 앞에 삽입) (다현, 화사)
    if (head.data == findData) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node) # 안 중요!(생략 가능)
        return
    # Case2 : 찾는 애가 중간 노드 (사나, 솔라)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)  # 안 중요!(생략 가능)
            return
    # Case3 : 없는 노드 앞에 삽입 (재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요!(생략 가능)
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    if (head.data == deleteData) :
        current = head
        head = head.link
        del(current)
        return
    current = head
    while(current.link != None):
        pre = current
        current = current.link
        if(current.data == deleteData):
            pre.link = current.link
            del(current)
            return

def findNode(finddata):
    global memory, head, pre, current
    current = head
    if(current.data == finddata) :
        return current
    while(current.link != None):
        current = current.link
        if(current.data == finddata):
            return current
    return Node()

## 변수
memory = []
head, pre, current = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 여러분 데이터!

## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요!(생략 가능)

for data in dataArray[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요!(생략 가능)
printNodes(head)

# insertNode('다현', '화사') # 찾을데이터, 삽입할데이터
# printNodes(head)
# insertNode('사나', '솔라') # 찾을데이터, 삽입할데이터
# printNodes(head)
#insertNode('재남', '문별') # 찾을데이터, 삽입할데이터
#printNodes(head)

#deleteNode('다현')
#printNodes(head)

retNode = findNode('사나')
print(retNode.data,' 뮤비가 나옵니다.~~ 쿵짝쿵짝')