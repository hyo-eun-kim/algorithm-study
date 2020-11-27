'''
leetcode 622
https://leetcode.com/problems/design-circular-queue/

Design your implementation of the circular queue.
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle
and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.

'''
# Queue : LILO, FIFO
# 68ms, faster than 70.89%
class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.len = k                        # circular queue의 길이
        self.data = [0 for _ in range(k)]   # 배열 이용해 circular queue 구현
        self.front = 0                      # 다음 pop할 위치
        self.rear = 0                       # 다음 push할 위치
        self.full = False                   # state of queue

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.front == self.rear and self.full:
            return False
        self.data[self.rear] = value
        self.rear = (self.rear+1) % self.len
        if self.front == self.rear:
            self.full = True
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.front == self.rear and not self.full:
            # queue가 비어있는 경우
            return False
        return_val = self.data[self.front]
        self.front = (self.front+1) % self.len
        if self.front == self.rear:
            self.full = False
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.front == self.rear and not self.full:
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.front == self.rear and not self.full:
            return -1
        return self.data[self.rear-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear and not self.full

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.front == self.rear and self.full


if __name__ == "__main__":
    circularQueue = MyCircularQueue(5)
    print(circularQueue.enQueue(10))    # True
    print(circularQueue.enQueue(20))    # True
    print(circularQueue.enQueue(30))    # True
    print(circularQueue.enQueue(40))    # True
    print(circularQueue.Rear())         # 40
    print(circularQueue.isFull())       # False
    print(circularQueue.deQueue())      # True
    print(circularQueue.deQueue())      # True
    print(circularQueue.enQueue(50))    # True
    print(circularQueue.enQueue(60))    # True
    print(circularQueue.Rear())         # 60
    print(circularQueue.Front())        # 30


