class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iterative
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev
        
