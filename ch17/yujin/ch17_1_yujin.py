# leetcode 58
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        """
        비교 후 정렬하며 병합 (얘도 재귀호출)
        """
        if l1 and l2:
            if l1.val > l2.val:# swap 조건
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2) # 병합하는 부분

        return l1 or l2 # none이 아닌 걸 리턴하게 됨 (둘 다 none이 아닐 경우에는 l1이 먼저 리턴)

    def sortList(self, head: ListNode) -> ListNode:
        """
        # 분할 지점을 찾기 위해 런너기법을 사용한다

        def partition(head):
            slow = fast = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            # while loop이 끝나면 slow는 연결리스트 중간 지점에 도착할 것
            return slow

        med = slow

        while med.next:
            med = partition()
        """
        if not (head and head.next): # 재귀 종료 조건 (next도 체크 안해주면 med.next에서 Nonetype object has no attribute 'next' error 뜸)
            return head

        med, slow, fast = None, head, head

        while fast and fast.next: # 런너
            med, slow, fast = slow, slow.next, fast.next.next

        med.next = None # 아예 head 노드가 가리키는 연결리스트 자체를 반쪽으로 쪼개버림
        # 뒷부분은 slow가 이미 가리키고 있기 때문에 상관이 없음

        l1 = self.sortList(head) # 앞부분
        l2 = self.sortList(slow) # 뒷부분

        return self.mergeTwoLists(l1, l2)


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        """
        리스트로 돌려서 풀기
        """
        if not (head and head.next): # 빈 리스트나 하나의 노드만 인풋으로 들어올 때 예외처리
            return head

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort() # sort하기

        # 다시 연결리스트로 더하기
        head_p = head = ListNode(val = arr[0])
        for i in range(1,len(arr)):
            head.next = ListNode(val = arr[i])
            head = head.next

        return head_p
