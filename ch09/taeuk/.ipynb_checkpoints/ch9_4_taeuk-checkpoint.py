'''
23. 큐를 이용한 스택 구현

큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
'''

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        # 여기서 순서를 뒤집어줌에 따라 가장 늦게 추가된 요소가 맨 앞에 오게 된다.
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
            
    def pop(self) -> int:
        # popleft을 하면 가장 늦게 추가된 요소인 맨 앞이 날아가기 때문에 stack과 같다.
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        # 바뀐 q의 맨 앞이 stack에서의 가장 늦게 쌓은것.(top)
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0

    # 32 ms
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()