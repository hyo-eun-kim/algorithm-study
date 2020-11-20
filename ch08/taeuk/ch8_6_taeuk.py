'''
18. 홀짝 연결 리스트

연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
'''

# 내 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        
        while head:
            # odd와 even에 초기값을 넣어 줌
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            # even 값이 존재한다면 head를 두 칸 뒤로 이동
            if even:
                head = head.next.next
            else:
                head = None
        # odd와 even을 이어준다.
        odd.next = dummy2.next
        return dummy1.next
    # 32 ms

# 반복 구조로 홀짝 노드 처리(다른 풀이)
class Solution:
    def oddEvenList(self, head : ListNode) -> ListNode:
        # 예외처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        # 홀수 노드의 마지막을 찍수 헤드로 연결
        odd.next = even_head
        return head
    # 40 ms