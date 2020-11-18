"""
## 8-3. 역순 연결 리스트

연결 리스트를 뒤집어라
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 리스트로 변환하여 reverse
        # 40 ms
        lst = []

        node = head
        while node:
            lst.append(node.val)
            node = node.next

        lst = lst[::-1]

        if not lst:
            return None

        rev = ListNode(lst[0])
        rev_node = rev
        for i in lst[1:]:
            rev_node.next = ListNode(i)
            rev_node = rev_node.next

        return rev

    def reverseList2(self, head: ListNode) -> ListNode:
        # 재귀 구조
        # 36ms
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    def reverseList3(self, head: ListNode) -> ListNode:
        # 반복 구조
        # 28ms
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev