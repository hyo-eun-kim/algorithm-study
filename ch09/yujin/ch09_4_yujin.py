class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

        """
        이걸 여기에 갖다 붙이면 push를 반복적으로 하는 걸 못잡아냄
        if self.s2 == []:
            while self.s1:
                self.s2.append(self.s1.pop())
        """

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.s2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop()) # 가장 먼저 들어간 게 가장 마지막에 붙어 있는 구조
        return self.s2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1 == [] and self.s2 == [] # 두 가지 길이 모두 체크
