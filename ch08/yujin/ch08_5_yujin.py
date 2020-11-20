class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = head
        while res and res.next:
            res.val, res.next.val = res.next.val, res.val

            res = res.next.next

        return head
        
