'''
14. 두 정렬 리스트의 병합

정렬되어 있는 두 연결 리스트를 합쳐라.
'''

# 내 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # l1과 l2의 마지막 값이 같을 경우 이걸 해줘야 마지막값까지 붙어서 나옴
        cur.next = l1 or l2
        # 데이터를 계속 쌓아두었던 dummy 리턴.
        return dummy.next
        
# 재귀 구조로 연결
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(se1f, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.va1 > l2.va1):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
    return l1