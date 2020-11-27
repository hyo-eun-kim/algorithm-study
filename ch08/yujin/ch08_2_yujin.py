# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        일단 갖다 붙인 다음에 다시 sort -> 정렬 과정을 거치기 때문에 최소 O(nlogn)의 시간복잡도를 가질 것.
        그럼 원소를 각각 비교해서 갖다 new list를 새로 만드는 과정도 있을 것
        """

        # empty 처리
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        hp = new = ListNode(None) # hp 놓기

        # 왜 이렇게 다 쪼개야 돌아가고 다중할당을 하면 오히려 안돌아갈까 근데 앞에 코드에서는 다중할당을 해야만 돌아갔잖아?
        while l1 and l2: # 리스트가 하나라도 끝나면 while loop 탈출
            #print(l1.val, l2.val)
            if l1.val < l2.val: # l1 next를 l2로 변경해야함
                new.next = l1
                new = new.next
                l1 = l1.next
            elif l1.val > l2.val:
                new.next = l2
                new = new.next
                l2 = l2.next # l2의 원소가 하나일 때는 이때 l2가 None이 되게 됨.
            else:
                new.next = l1
                new = new.next
                l1 = l1.next
                new.next = l2
                new = new.next
                l2 = l2.next

        if l1: # if l2 is empty
            new.next = l1
        elif l2: # l1 is empty
            new.next = l2


        return hp.next

        def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        List로 자료형 변환한 다음에 다시 linked list
        """
        def get_linked_list(lst, idx):
            if idx == len(lst): # 마지막 노드 처리
                return None
            else:
                return ListNode(lst[idx], get_linked_list(lst, idx+1))

        list1, list2, new = [], [], None

        while l1:
            list1.append(l1.val)
            l1 = l1.next

        while l2:
            list2.append(l2.val)
            l2 = l2.next


        new = get_linked_list(sorted(list1+list2), 0)

        return new
