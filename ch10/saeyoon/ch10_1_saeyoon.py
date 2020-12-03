"""
## 10-1. 원형 데크 디자인

다음 연산을 제공하는 원형 데크를 디자인하라.
- MyCircularDeque(k) : 데크사이즈를 k로 지정하는 생성자다.
- insertFront( ): 데크 처음에 아이템올 추가하고 성공할 경우 true를 리턴한다
- insertLast ( ): 데크 마지막에 아이템올 추가하고 성공할 경우 true를 리턴한다.
- deleteFront( ): 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
- deleteLast( ): 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
- getFront( ): 데크의 첫 번째 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
- getRear( ): 데크의 마지막 아이 템을 가져온다 데크가 비어 있다면 -1을 리턴한다.
- isEmpty( ): 데크가 비어 있는지 여부를 판별한다.
- isFull( ) 데크가 가득 차 있는지 여부를 판별한다.
"""
from typing import *

# 이중 연결 리스트
class ListNode:
    def __init__(self, value):
        self.val = value
        self.right = self.left = None

class MyCircularDeque:
    # 80ms
    def __init__(self, k: int):
        self.head = self.tail = ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head
        self.k = k
        self.size = 0

    def add(self, prenode: ListNode, new: ListNode):
        n = prenode.right
        prenode.right = new
        new.left, new.right = prenode, n
        n.left = new

    def remove(self, prenode: ListNode):
        n = prenode.right.right
        prenode.right = n
        n.left = prenode

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        self.add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        self.add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.remove(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.remove(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.size else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


class MyCircularDeque2:
    # 60ms
    def __init__(self, k: int):
        self.front, self.rear = 0, 0
        self.k = k
        self.size = 0
        self.data = [-1] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[self.front] = value
        else:
            self.front = (self.front - 1) % self.k
            self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.data[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.rear] = -1
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True

    def getFront(self) -> int:
        return self.data[self.front]

    def getRear(self) -> int:
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


if __name__ == '__main__':
    obj = MyCircularDeque(3)
    print(obj.insertLast(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
    print(obj.insertFront(4))
    print(obj.deleteFront())
    print(obj.getRear())
    print(obj.isFull())
    print(obj.deleteLast())
    print(obj.getFront())
    print(obj.isEmpty())