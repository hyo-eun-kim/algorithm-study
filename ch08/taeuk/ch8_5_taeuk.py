'''
17. 페어의 노드 스왑

연결 리스트를 입력받아 페어 단위로 스왑하라.
'''

# 내 풀이(반복 구조로 스왑)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # dummy를 설정해준다. root에 쌓일 예정
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 head를 가리키도록 해줌.(b는 원래 head의 next)
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            # prev를 다음 계산을 위해 두칸 뒤로 이동
            prev = prev.next.next
            # head도 이동
            head = head.next
        return root.next
    # 28 ms

# 값만 교환
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head
    # 32 ms

# 재귀 구조로 스왑
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
    # 28 ms