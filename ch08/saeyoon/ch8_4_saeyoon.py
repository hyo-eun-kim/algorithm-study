"""
## 8-4. 두 수의 덧셈

역순으로 저장된 연결리스트의 숫자를 더하라.
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> List:
        # 리스트로 변환하여 reverse하고 리스트 형태로 반환
        lst = []

        node = head
        while node:
            lst.append(node.val)
            node = node.next

        return lst[::-1]

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 76ms
        rev1 = self.reverseList(l1)
        rev2 = self.reverseList(l2)

        result = str(int(''.join(str(i) for i in rev1)) + int(''.join(str(i) for i in rev2)))

        if not result:
            return None

        result = result[::-1]

        head = ListNode(result[0])
        node = head
        for i in result[1:]:
            node.next = ListNode(i)
            node = node.next

        return head