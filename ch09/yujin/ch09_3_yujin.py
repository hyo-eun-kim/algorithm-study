class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.

        queue 자료형을 이용해서 stack을 구현해야 하니까 init은 queue로 함
        """
        self.q = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        #self.q.appendleft(x)



    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        tmp = self.q.pop()
        self.q.append(tmp)
        return tmp


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0
