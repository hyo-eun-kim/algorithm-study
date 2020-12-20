'''
https://leetcode.com/problems/merge-k-sorted-lists/
'''

from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 104ms, 18.2MB
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        heap = []
        for cur_list in lists:
            cur_node = cur_list
            while cur_node != None:
                heapq.heappush(heap, cur_node.val)
                cur_node = cur_node.next

        # 파이썬에서의 heapq는 min heap이기 때문에
        # pop하면 가장 작은값부터 나온다.
        return_list = cur_node = ListNode()
        while heap:
            value = heapq.heappop(heap)
            cur_node.next = ListNode(value)
            cur_node = cur_node.next

        return return_list.next

# 92ms, 18.1MB
class Solution2:
    def mergeKLists(self, lists) -> ListNode:
        root = cur_node = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                # linked list의 root를 heap에 저장
                # i를 저장하는 이유는 value가 같을 때 priority를 부여할 수 없기 때문이다.
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            # root가 가장 작은 값을 가진 linked list부터 나온다
            node = heapq.heappop(heap)
            idx = node[1]
            cur_node.next = node[2]

            cur_node = cur_node.next
            if cur_node.next:
                heapq.heappush(heap, (cur_node.next.val, idx, cur_node.next))

        return root.next

