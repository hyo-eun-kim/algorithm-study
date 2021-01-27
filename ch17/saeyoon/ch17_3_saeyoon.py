"""
## 17-3. 삽입 정렬 리스트

연결 리스트를 삽입 정렬로 정렬하라.
"""
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 시간 초과
        result = []
        node = head
        while node:
            result.append(node.val)

        for i in range(1, len(result)):
            for j in range(i, 0, -1):
                if result[j-1] > result[j]:
                    result[j-1], result[j] = result[j], result[j-1]

        node = head
        for i in result:
            node.val = i
            node = node.next
        return head

    def insertionSortList2(self, head: ListNode) -> ListNode:
        # node: 정렬 연결 리스트 추가해주는 포인터
        # result: 정렬 연결 리스트의 head
        node = result = ListNode(0)
        while head:
            while node.next and node.next.val < head.val:
                node = node.next

            node.next, head.next, head = head, node.next, head.next

            if head and node.val > head.val:
                node = result

        return result.next


if __name__ == '__main__':
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sol = Solution()
    print(sol.insertionSortList(head))