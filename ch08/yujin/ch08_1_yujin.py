# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None: # empty 처리 해줘야함.
            return True
        res = [head.val]
        while True:
            if head.next == None:
                break
            res.append(head.next.val)
            head = head.next
        print(res)
        return res == res[::-1]

# 말단 노드부터 정의해야하는 구조인 듯..?
#node4 = ListNode(val = 1, next = None)
node3 = ListNode(val = 2, next = None)
#node2 = ListNode(val = 2, next = node3)
node1 = ListNode(val = 1, next = node3)


sol = Solution()
print(sol.isPalindrome([]))
