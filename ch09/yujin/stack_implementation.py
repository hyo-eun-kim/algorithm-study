# stack python implementation
class Node:
    def __init__(self, item, next):
        """
        item: 노드의 값
        next: 다음 노드를 가리키는 포인터
        """
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last) # LIFO

    def pop(self):
        item = self.last.item
        self.last = self.last.next # 이전 노드로 stack pointer 이동
        return item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())
