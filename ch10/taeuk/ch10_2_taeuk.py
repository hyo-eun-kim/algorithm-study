'''
27. k개 정렬 리스트 병합

k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
'''

# 내 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        
        for i in lists:
            while i:
                self.nodes.append(i.val)
                i = i.next
        
        for j in sorted(self.nodes):
            point.next = ListNode(j)
            point = point.next
        
        return head.next
    # 92 ms

    
# 우선순위 큐를 활용한 풀이
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i , lists[i]))
        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result. next :
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next
    # 92 ms
