'''
leetcode 225

Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

You must use only standard operations of a queue,
which means only push to back, peek/pop from front, size, and is empty operations are valid.
'''
from collections import deque


class MyStack:
    def __init__(self):
        self.data = deque()

    def push(self, x):
        self.data.appendleft(x)
        for i in range(len(self.data)-1):
            self.data.appendleft(self.data.pop())

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0


if __name__ == "__main__":
    stack = MyStack()

    stack.push(1);
    stack.push(2);
    print(stack.top())      # 2
    print(stack.pop())      # 2
    print(stack.empty())    # False