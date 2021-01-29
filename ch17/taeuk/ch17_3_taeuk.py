'''
60. 삽입 정렬 리스트

연결 리스트를 삽입 정렬로 정렬하라.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val: 
                
                cur = cur.next
                
            cur.next, head.next, head = head, cur.next, head.next
            if head and cur.val > head.val:
                cur = dummy
        return dummy.next
    # 176 ms