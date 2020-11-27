class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.cq = []
        self.size = k


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.cq) < self.size:
            self.cq.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        try:
            del self.cq[0]
            return True
        except:
            return False


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        try:
            return self.cq[0]
        except IndexError:
            return -1


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        try:
            return self.cq[-1]
        except:
            return -1


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.cq) == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.cq) == self.size
