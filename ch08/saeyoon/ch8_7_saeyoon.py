"""
## 8-7. 역순 연결 리스트 II

인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 32ms
        if not head:
            return None

        lst = []
        node = head
        while node:
            lst.append(node.val)
            node = node.next

        rev_lst = lst[:m - 1] + lst[m - 1:n][::-1] + lst[n:]

        rev_head = ListNode(rev_lst[0])
        rev_node = rev_head
        for i in rev_lst[1:]:
            rev_node.next = ListNode(rev_lst[i])
            rev_node = rev_node.next

        return rev_head