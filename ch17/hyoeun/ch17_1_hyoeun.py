'''
58. 리스트 정렬
연결리스트를 O(NlogN)에 정렬하라.
https://leetcode.com/problems/sort-list/

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        sorted_list = []
        while cur:
            sorted_list.append(cur.val)
            cur = cur.next
        sorted_list.sort()

        cur = head
        for i in range(len(sorted_list)):
            cur.val = sorted_list[i]
            cur = cur.next
        return head


class Solution2:
    def merge(self, h1, h2):
        dummy = cur = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next

        cur.next = h1 or h2  # h1이 남아있으면 h1, 아니면 h2
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            half = slow
            slow = slow.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)