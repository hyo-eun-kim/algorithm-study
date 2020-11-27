"""
## 9-6. 원형 큐 디자인

원형 큐를 디자인하라.

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
"""
from typing import *

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.max = k
        self.size = self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max
        self.q[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.front + 1) % self.max]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.rear) % self.max]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max


class MyCircularQueue2:
    # size 변수 없이 구현
    # 실제로 front 변수는 첫번째 원소의 이전을 가리키며
    # 환형 큐는 꽉 차있는지 확인을 위해 최대 원소 수보다 하나 큰 크기의 큐를 가짐
    def __init__(self, k: int):
        self.q = [None] * (k+1)
        self.max = k+1
        self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max
        self.q[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.front + 1) % self.max]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.rear) % self.max]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.max


if __name__ == '__main__':
    cq = MyCircularQueue(3)
    print(cq.enQueue(1)) # return True
    print(cq.enQueue(2)) # return True
    print(cq.enQueue(3)) # return True
    print(cq.enQueue(4)) # return False, the queue is full
    print(cq.Rear()) # return 3
    print(cq.isFull()) # return True
    print(cq.deQueue()) # return True
    print(cq.enQueue(4))  # return True
    print(cq.Rear()) # return 4
    print(cq.Front())  # return 2

    cq2 = MyCircularQueue(3)
    print(cq2.enQueue(1)) # return True
    print(cq2.enQueue(2)) # return True
    print(cq2.enQueue(3)) # return True
    print(cq2.enQueue(4)) # return False, the queue is full
    print(cq2.Rear()) # return 3
    print(cq2.isFull()) # return True
    print(cq2.deQueue()) # return True
    print(cq2.enQueue(4))  # return True
    print(cq2.Rear()) # return 4
    print(cq2.Front())  # return 2