'''
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
역순으로저장된 연결 리스트의 숫자를더하라 .

Input: l1 = [2,4,3], l2 = [5,6,4]           Output: [7,0,8] :   Explanation: 342 + 465 = 807.
Input: l1 = [0], l2 = [0]                   Output: [0]
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = cur = ListNode()
    carry = 0
    while l1 is not None or l2 is not None:
        # l1, l2의 길이가 동일하지 않은 경우 대비
        l1_value = 0 if l1 is None else l1.val
        l2_value = 0 if l2 is None else l2.val

        s = l1_value + l2_value + carry
        s, carry = s % 10, s // 10  # sum, carry 계산

        cur.next = ListNode(s) # 새 노드 생성하여 끝에 추가
        cur = cur.next

        l1 = l1 if l1 is None else l1.next
        l2 = l2 if l2 is None else l2.next

    if carry:
        # 만약 마지막 노드에서 carry 발생했다면 다음과 같이 추가
        cur.next = ListNode(carry)
    return head.next # 첫 노드는 dummy node


if __name__ == "__main__":
    l1 = l1_cur = ListNode()
    for val in [9, 9, 9, 9, 9, 9, 9, 9]:
        l1_cur.next = ListNode(val)
        l1_cur = l1_cur.next

    l2 = l2_cur = ListNode()
    for val in [9, 9, 9, 9]:
        l2_cur.next = ListNode(val)
        l2_cur = l2_cur.next

    sum_list = addTwoNumbers(l1.next, l2.next)
    while sum_list:
        print(sum_list.val)
        sum_list = sum_list.next