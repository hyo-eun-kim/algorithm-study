'''
26. 다음 연산을 제공하는 원형 데크를 디자인하라.

MyCircularDeque(k) : 데크 사이즈를 k로 지정하는 생성자다.
insertFront(): 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴한다.
insertLast(): 데크 마지막에 아이템올 추가하고 성공할 경우 true를 리턴한다.
deleteFront(): 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
deleteLast(): 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
getFront(): 데크의 첫 번째 아이템을 가져온다. 데크가 비어 있다면 - 1을 리턴한다.
getRear(): 데크의 마지막 아이템을 가져온다 데크가 비어 있다면 -1을 리턴한다.
isEmpty(): 데크가 비어 있는지 여부를 판별한다.
isFull(): 데크가 가득 차 있는지 여부를 판별한다.
'''

# 풀이
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        
    
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
        
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node
    

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.len == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.len == self.k
    # 76 ms


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
    