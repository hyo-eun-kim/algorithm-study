# K 개의 정렬 리스트 병합
# K 개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라. 

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:

    def mergeKLists(self,lists):

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = result = ListNode(None)
        heap = []

        for i, lst in enumerate(lists): # heap 에 lst 를 저장 ,
            if lst:
                heapq.heappush(heap,(lst.val, i,lst))  # 값이 똑같았을때, index로 한번더 비교할수 있게.

        while heap:
                                        # root 가 가장 작은 값을 가진 linked list 부터 나온다.
            node = heapq.heappop(heap)  # 힙 에서는 heappop을 통해서 가장 작은 원소를 삭제하고,heap[0] 을 통해 최솟값에
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next :
                heapq.heappush(heap,(result.next.val , idx, result.next))

        return root.next



