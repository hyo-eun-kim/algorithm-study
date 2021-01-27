"""
## 17-1. 리스트 정렬

연결 리스트를 O(nlogn)에 정렬하라
"""
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 156ms
        result = []
        node = head
        while node:
            result.append(node.val)
            node = node.next

        result.sort()

        node = head
        for i in result:
            node.val = i
            node = node.next

        return head


if __name__ == '__main__':
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sol = Solution()
    print(sol.sortList(head))