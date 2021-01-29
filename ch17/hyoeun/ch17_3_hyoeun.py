'''
60. 삽입 정렬 리스트
연결리스트를 삽입 정렬으로 정렬하라.
https://leetcode.com/problems/insertion-sort-list/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        sorted_before = dummy = ListNode()
        sorted_cur = dummy.next
        unsorted_cur = head

        while unsorted_cur:
            if sorted_cur and sorted_cur.val > unsorted_cur.val:
                # sorted의 처음부터 비교하기 (항상 처음부터 비교하는 것을 막기 위해서)
                sorted_before, sorted_cur = dummy, dummy.next
            while sorted_cur and sorted_cur.val <= unsorted_cur.val:
                # 나보다 처음으로 큰 노드가 나올때까지 전진
                sorted_before = sorted_cur
                sorted_cur = sorted_cur.next

            # linked list에서의 insert 진행하기
            temp = unsorted_cur.next
            unsorted_cur.next = sorted_before.next
            sorted_cur = sorted_before.next = unsorted_cur
            unsorted_cur = temp

        return dummy.next


