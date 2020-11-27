# 큐를 이용한 스택 구현
# 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
import collections
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)   
        #print("append", self.q)

        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())  # 방금 삽입한 요소를 맨 앞에 두는 상태로 재 정렬한다.
        #    print(i,self.q)
        #print("result", self.q)    
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return print(self.q.popleft())

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return print(self.q[0])
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return print(len(self.q)==0)
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
obj.top()
obj.empty()