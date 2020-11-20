# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = ListNode()
        # new 초기값 할당
        if l1.val < l2.val:
            new = l1
            l1, new = l1.next, new.next
        elif l1.val > l2.val:
            new = l2
            l2, new = l2.next, new.next
        else:
            new, new.next = l1, l2
            l1, l2, new = l1.next, l2.next, new.next

        # 만들어가기
        while l1 and l2: # 리스트가 하나라도 끝나면 while loop 탈출
            if l1.val < l2.val:
                new.next = l1
                l1, new = l1.next, new.next
            elif l1.val > l2.val:
                new.next = l2
                l2, new = l2.next, new.next
            else:
                new.next, new.next.next = l1, l2
                l1, l2, new = l1.next, l2.next, new.next.next

        if l1:
            new.next = l1
        else:
            new.next = l2

        return new

sol = Solution()

lst1 = [1,2,4]
lst2 = [1,3,4]
node1 = ListNode()
node2 = ListNode()

for i in range(len(lst1)):
    if node1.next != None:
        node1.val, node1.next = lst1[i], ListNode()
        node1 = node1.next

while node1:
    print(node1.val)
    node1 = node1.next
"""
new = sol.mergeTwoLists([1,2,4],[1,3,4])
while new:
    print(new.val)
    new = new.next
"""
