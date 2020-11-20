# 팰린드롬 연결리스트
# 연결리스트가 팰린드롬 구조인지 판별하라
import collections
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

node1 = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4


def isPalindrome(head):

    q = collections.deque()  # 이거를 이렇게 하면 엄청 빨라짐!!!!
    if not head :
        return True

    node = head
    
    while node is not None : # None : 값 자체가 정의되어있지 않다. is로만 비교 가능 
        q.append(node.val)
        node= node.next
    print(q)

    while len(q) > 1 :
        if q.popleft() != q.pop():  # 기억하자 popleft

            return False
        else :
            return True

isPalindrome(node1)
