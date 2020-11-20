"""
## 8-6. 홀짝 연결 리스트

연결 리스트를 입력받아 페어 단위로 스왑하라
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 36ms
        # 15.7mb
        if not head:
            return None

        odd_head, even_head = head, head.next
        odd_node, even_node = odd_head, even_head

        while even_node and even_node.next:
            odd_node.next = odd_node.next.next
            odd_node = odd_node.next
            even_node.next = even_node.next.next
            even_node = even_node.next

        odd_node.next = even_head

        return odd_head