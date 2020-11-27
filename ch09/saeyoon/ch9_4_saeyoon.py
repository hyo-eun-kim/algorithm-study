"""
## 9-4. 큐를 이용한 스택 구현

큐를 이용해 다음 연산을 지원하는 스택을 구현하라.

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
"""
from typing import *
from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # for i in range(len(self.q) - 1):
        #     self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top()) # 2
    stack.pop()
    print(stack.top()) # 1
    print(stack.empty()) # False
    stack.pop()
    print(stack.empty()) # True
