# 두 정렬 리스트의 병합
# 정렬되어있는 두 리스트를 연결하라!

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

node1 = Node(1)
node2 = Node(2)
node3 = Node(4)
node1.next = node2
node2.next = node3

node4 = Node(1)
node5 = Node(3)
node6 = Node(4)
node4.next = node5
node5.next = node6

def mergeTwoLists(l1, l2):
    if l1 is None :
        return l2
    
    if l2 is None :
        return l1
    
    if l1.val <= l2.val :
        head = l1
        head.next = mergeTwoLists(l1.next, l2)
    else :
        head =l2
        head.next = mergeTwoLists(l1,l2.next)
    return head


mergeTwoLists(node1, node4)