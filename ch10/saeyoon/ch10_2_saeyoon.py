"""
## 10-2. k개의 정렬 리스트 병합

k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
"""
from typing import *
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 96ms
        head = point = ListNode(None)
        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
                # 우선순위 큐의 경우 대소 비교가 가능한 인덱스가 존재해야 함

        while heap:
            val, idx, node = heapq.heappop(heap)
            point.next = node
            point = point.next
            if point.next:
                heapq.heappush(heap, (point.next.val, idx, point.next))

        return head.next


if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeKLists([[1,4,5],[1,3,4],[2,6]]))