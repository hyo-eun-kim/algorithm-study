# 원형 큐 디자인
# 원형 큐를 디자인 하라 

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.q = [None]*k
        self.maxlen = k 
        self.front = 0
        self.rear = 0

    def enQueue(self, value):  # 요소 삽입
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.q[self.rear] is None : # rear가 비어있으면
            self.q[self.rear] = value
            self.rear = (self.rear+1) % self.maxlen   # 나머지 값을 이용해서 빙글빙글 돌수 있게
            return True
        else: 
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.q[self.front] is None : # front 에 값이 없다는건 deQueue를 할수 없다.
            return False
        else :
            self.q[self.front] = None # 값을 비우고 
            self.front = (self.front+1) % self.maxlen # 앞으로 포인터 이동
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.q[self.front] is None else self.q[self.front]
        

    def Rear(self): 
        """
        Get the last item from the queue.
        :rtype: int
        """
        return -1 if self.q[self.rear-1] is None else self.q[self.rear-1]  # rear 는 넣고 싶은 곳의 포인터를 가르키고 있으므로 -1 한거의 값을 가져옴.
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.rear == self.front and self.q[self.rear] is None
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.rear == self.front and self.q[self.rear] is not None
        