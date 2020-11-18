"""
## 8-2. 팰린드롬 연결 리스트

연결 리스트가 팰린드롬 구조인지 판별하라
"""
from typing import *
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def is_palindrome(head: ListNode) -> bool:
        # List 타입으로 풀이
        # 68ms
        lst = []

        if not head:
            return True

        node = head
        while node is not None:
            lst.append(node.val)
            node = node.next

        return True if lst == lst[::-1] else False


    def is_palindrome2(head: ListNode) -> bool:
        # Deque 타입으로 풀이
        # 60ms
        deq = deque()

        if not head:
            return True

        node = head
        while node is not None:
            deq.append(node.val)
            node = node.next

        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False

        return True


    def is_palindrome3(head: ListNode) -> bool:
        # Runner 기법 활용
        # 64ms
        rev = None
        slow = fast = head

        # fast와 fast.next가 가리키는 노드가 None이 아닐 때까지
        while fast and fast.next:
            # fast는 두 칸씩 이동
            fast = fast.next.next
            # slow는 한 칸씩 이동하며 rev(역순 연결리스트)를 만들어 나감
            rev, rev.next, slow = slow, rev, slow.next

        # 길이가 홀수일 때는 slow가 한 칸 더 앞으로 이동하여야 중앙임
        if fast:
            slow = slow.next

        # slow의 나머지 이동 경로와 rev 연결리스트의 값을 비교함
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev
