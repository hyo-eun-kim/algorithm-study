"""
## 8-2. 두 정렬 리스트의 병합

정렬되어 있는 두 연결 리스트를 합쳐라.
"""
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 두 리스트 합해서 정렬
        # 32ms
        lst1, lst2 = [],[]
        while l1:
            lst1.append(l1.val)
            l1 = l1.next

        while l2:
            lst2.append(l2.val)
            l2 = l2.next

        lst = lst1 + lst2
        lst.sort()

        if not lst:
            return None

        head = ListNode(lst[0])
        node = head
        for i in lst[1:]:
            node.next = ListNode(i)
            node = node.next

        return head


def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 재귀
    # 32ms
    if (not l1) or (l1.val > l2.val and l2):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists2(l1.next, l2)

    return l1