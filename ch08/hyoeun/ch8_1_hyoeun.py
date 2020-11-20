'''
https://leetcode.com/problems/palindrome-linked-list/
연결리스트가 팰린드롬 구조인지 판별하라
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    deq = deque()
    # 양방향에서 삽입/삭제할 수 있는 자료구조
    # Q. 왜 list 대신 deq를 사용하면 성능이 향상되는가?
    # A. list에서 가장 앞에 위치한 원소를 pop하면 shift가 일어나며 O(n) 소요
    #    반면, deque는 가장 앞에 위치한 원소 pop하면 O(1)

    # 1. linked list의 모든 원소를 deque로 옮긴다
    node = head
    while node != None:
        deq.append(node.val) # 끝에 삽입
        node = node.next

    # 2. 양방향에서 pop하며 동일하지 않다면 그 즉시 False return
    while len(deq) > 1:
        # 입력으로 받는 node의 개수가 홀수/짝수인 경우 모두 고려하기 위해
        # len(deq) > 1 이면 loop를 돌도록 코드 작성
        right_val = deq.pop()
        left_val = deq.popleft()
        if right_val != left_val:
            return False
    return True


# 이건 스터디 전 다시 해보기!
def runner_solution(head: ListNode) -> bool:
    # 1. slow runner, fast runner head로 초기화
    slow, fast = head, head
    rev = None # reversed linked list

    # reversed linked list 구성
    while fast and fast.next:
        # 여기서 fast runner는 linked list의 절반 지점을 체크하기 위하여 사용
        fast = fast.next.next  # 2 step 이동
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next  # 홀수 길이의 linked list 받은 경우를 위해

    while rev and rev.val == slow.val:
        rev, slow = rev.next, slow.next
    return not rev


if __name__ == "__main__":
    Node1 = ListNode(1)
    Node2 = ListNode(2, Node1)
    Node3 = ListNode(2, Node2)
    head = ListNode(1, Node3)

    print(isPalindrome(head))
