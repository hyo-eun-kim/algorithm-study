'''
16. 두 수의 덧셈

역순으로 저장된 연결 리스트의 숫자를 더하라.
'''

# 내 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(str(l1.val))
            l1 = l1.next
        l1_list = int(''.join(l1_list[::-1]))
        
        while l2:
            l2_list.append(str(l2.val))
            l2= l2.next
        l2_list = int(''.join(l2_list[::-1]))
        
        
        prev: ListNode = None
        for i in str(l1_list + l2_list):
            node = ListNode(i)
            node.next = prev
            prev = node
        return prev
# 76 ms

# 자료형 변환(내 풀이와 유사하지만 다른 구조로 짬)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
                      
    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
                             
        return node
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode :
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))
# 80 ms
    
# 전가산기 구현
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두입력값의합계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next
# 68 ms