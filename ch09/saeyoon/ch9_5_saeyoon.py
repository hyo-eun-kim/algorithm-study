"""
## 9-5. 스택을 이용한 구현

스택을 이용해 다음 연산을 지원하는 큐를 구현하라.

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""
from typing import *


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1) # queue is [1]
    queue.push(2) # queue is [1, 2]
    print(queue.peek()) # return 1
    queue.pop() # return 1, queue is [2]
    print(queue.peek()) # return 2
    print(queue.empty()) # False
    queue.pop() # return 2, queue is []
    print(queue.empty()) # True