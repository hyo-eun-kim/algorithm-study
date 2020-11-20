# 역순 연결 리스트
# 연결 리스트를 뒤집어라!
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def reverseList(head):
    
    node = head
    rev = None

    while node :
       next , node.next = node.next , rev
       rev,node = node,next
    return rev



    