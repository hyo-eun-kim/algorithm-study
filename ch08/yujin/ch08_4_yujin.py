class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 역으로 탐색해서 operand 만듦
        n1, n2, res = [],[],None
        tmp1, tmp2, sig = 0,0,0
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        while l2:
            n2.append(l2.val)
            l2 = l2.next

        for i in range(len(n1)):
            tmp1 += n1[i] * 10**(sig)
            sig += 1

        sig = 0

        for i in range(len(n2)):
            tmp2 += n2[i] * (10**sig)
            sig += 1

        tmp2 += tmp1
        tmp2 = list(map(int, list(str(tmp2)[::-1])))

        def get_linked_list(lst, idx):
            if idx == len(lst):
                return None
            else:
                return ListNode(lst[idx], get_linked_list(lst, idx+1))
        rev = get_linked_list(tmp2, 0)

        return rev
