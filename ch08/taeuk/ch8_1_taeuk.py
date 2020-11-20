'''
13. 팰린드롬 연결 리스트

연결 리스트가 팰린드롬 구조인지 판별하라.
'''

# 내 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
# 68ms
    
# 데크를 이용한 최적화
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 데크자료형선언
        q: Deque = collections.deque()
        if not head:
            return True
        node = head
        while node is not None :
            q.append(node.val)
            node = node.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
# 72ms
    
# 런너를 이용한 풀이
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next , slow = slow, rev, slow.next
        if fast :
            slow = slow.next
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next , rev.next
        return not rev
# 64ms