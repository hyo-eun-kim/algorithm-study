# 스택을 이용한 큐 구현
# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input =[]
        self.output = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.output.pop()    

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.input==[] and self.output==[]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

########################
class MyQueue(object):

    def __init__(self):
        self.lst = list()
        
    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop(0)

    def peek(self):
        return self.lst[0]

    def empty(self):
        return len(self.lst) == 0