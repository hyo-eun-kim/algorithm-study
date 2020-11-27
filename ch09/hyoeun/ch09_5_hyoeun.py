'''
leetcode 232
https://leetcode.com/problems/implement-queue-using-stacks/

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

You must use only standard operations of a stack,
which means only push to top, peek/pop from top, size, and is empty operations are valid.
'''

# push : append()
# pop : pop()
# 24ns (faster than 92.65%)
class MyQueue:
    def __init__(self):
        self.data = []

    def push(self, x):
        # ex) data = top [1, 2, 3, 4] bottom
        temp_stack = []
        while self.data:
            temp_stack.append(self.data.pop()) # temp_stack = top->[4, 3, 2, 1]<-bottom
        self.data.append(x) # data = top [x] bottom
        while temp_stack:
            self.data.append(temp_stack.pop())
        # data = top [1, 2, 3, 4, x] bottom

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

    def empty(self) -> bool:
        return len(self.data) == 0


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue.peek())     # 1
    print(queue.pop())      # 1
    print(queue.pop())      # 1
    print(queue.pop())      # 1
    print(queue.empty())    # False