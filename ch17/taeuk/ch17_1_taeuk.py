'''
58. 리스트 정렬

연결 리스트를 O(n log n)에 정렬하라.

Input: head = [4,2,1,3]
Output: [1,2,3,4]
'''

# 내 풀이

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
        
        lst.sort()
        
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        
        return head
    # 160 ms
    
    
# 병합 정렬을 이용한 풀이
class Solution():
    def mergeTwoLists(se1f, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = se1f.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head : ListNode) -> ListNode:
        if not (head and head.next):
            return head
        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next , fast.next.next
        half.next = None

        # 분할재귀호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)
    # 508 ms