'''
https://leetcode.com/problems/swap-nodes-in-pairs/
연결 리스트를 입력받아 페어 단위로 스왑하라 .
이 때 노드의 값을 바꾸는 게 아니라, 노드 그 자체가 변경되어야 한다.
Input: head = [1,2,3,4] Output: [2,1,4,3]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my solution
def swapPairs(head: ListNode) -> ListNode:
    new_head = ListNode()       # dummy node
    new_head.next = head
    cur_before = new_head       # 현재 노드의 이전 노드
    cur = cur_before.next       # 현재 노드

    while cur is not None and cur.next is not None:
        # cur이 None이거나 cur.next가 None이면 중지
        # 1. A - [B - C] - D -> A - [C - B] - D
        cur_next = cur.next  # C
        cur_before.next = cur_next  # A->C
        cur.next = cur_next.next if cur_next.next else None  # B->D
        cur_next.next = cur  # C->B

        cur_before = cur_before.next.next
        cur = cur_before.next
    return new_head.next


# 값만 교환하는 변칙적인 풀이
def solution_1(head: ListNode)->ListNode:
    cur = head
    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next
    return head


if __name__ == "__main__":
    head = cur = ListNode()
    for val in [1, 2, 3, 4]:
        cur.next = ListNode(val)
        cur = cur.next

    new_head = swapPairs(head.next)
    while new_head:
        print(new_head.val)
        new_head = new_head.next