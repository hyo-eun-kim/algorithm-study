# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        srt_p = srt = ListNode(0)
        while head:
            while srt.next and srt.next.val < head.val:
                srt = srt.next

            srt.next, head.next, head = head, srt.next, head.next

            if head and srt.val > head.val:
                srt = srt_p

        return srt_p.next
