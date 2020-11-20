'''
15. 역순 연결 리스트

연결 리스트를 뒤집어라.
'''

# 내 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            node = head
            head = head.next
            # 앞으로 쌓아간다.
            node.next = prev
            prev = node
        return prev
# 32 ms

# 재귀 구조로 뒤집기
class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:

        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)
# 36 ms

# 반복 구조로 뒤집기
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
# 28 ms