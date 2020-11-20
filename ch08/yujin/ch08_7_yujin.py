# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # empty 처리
        if not head or m == n:
            return head

        hp = start = ListNode() # head pointer -> head가 변경되기 때문에 값을 홀드하고 있어야함.
        hp.next = head
        tmp = None

        for _ in range(m-1):
            start = start.next
        end = start.next

        for _ in range(n-m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return hp.next
