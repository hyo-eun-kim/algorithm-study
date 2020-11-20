# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        홀짝 구분한 다음에
        이어붙이기
        홀짝 구분은 포인터 이동으로 가능
        """
        if not head: # head empty
            return None

        odd = head # head값을 변경시키기 위함
        even = head.next
        even_head_p = head.next # even의 헤드포인터를 하나 더 줘야 함. even 포인터는 변경되기 때문에 앞의 값을 잃어버릴 것.

        """
        # 이렇게 하면 안됨 (참조가 꼬임)
        while even and even.next: # 리스트 순회 완료할 때까지
            odd.next = odd.next.next # 두 칸씩 이동
            odd = odd.next
            even.next = even.next.next # 얘도 마찬가지
            even = even.next

        while even:
            print(even.val)
            even = even.next
        """

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head_p
        return head
