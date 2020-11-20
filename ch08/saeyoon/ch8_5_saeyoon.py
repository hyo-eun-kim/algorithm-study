"""
## 8-5. 페어의 노드 스왑

연결 리스트를 입력받아 페어 단위로 스왑하라
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 재귀
        # 24ms
        if head and head.next:
            new_head = head.next
            head.next = self.swapPairs(new_head.next)
            new_head.next = head
            return new_head

        return head