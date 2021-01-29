# 삽입정렬 리스트
# 연결리스트를 삽입정렬로 정렬하라.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = parent = ListNode(0)
        while head :  # head 는 정렬해야하는 대상, cur는 정렬을 끝낸 대상 
            while cur.next and cur.next.val <head.val: # head 보다 cur 이 작으면, 계속 cur 를 이동하면서 삽입할 위치 찾기
                cur = cur.next
            
            cur.next , head.next, head = head, cur.next, head.next  # 삽입될 위치를 찾았으면, 

           
            if head and cur.val>head.val :  #cur 가 head 보다 클때만 돌아가기!
                cur= parent  # 다시 처음으로 돌아가서 차례대로 비료

        return parent.next
    