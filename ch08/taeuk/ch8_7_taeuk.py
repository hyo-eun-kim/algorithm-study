'''
19. 역순 연결 리스트 2

인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
'''

# 내 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for i in range(m-1):
            prev = prev.next
        
        r = None
        cur = prev.next
        for i in range(n - m + 1):
            
            next = cur.next
            cur.next = r
            r, cur = cur, next
        
        prev.next.next = cur
        prev.next = r
        
        return dummy.next
    # 32 ms

# 반복 구조로 노드 뒤집기
class Solution:
    def reverseBetween(self , head: ListNode, m: int , n: int) -> ListNode:
        # 예외 처리
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next
        
        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next , end.next = start.next , end.next, end.next.next
            start.next.next = tmp
        return root.next
    # 28 ms