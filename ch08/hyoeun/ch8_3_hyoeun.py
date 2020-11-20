'''
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my solution
def reverseList(head: ListNode) -> ListNode:
    reversed_head = ListNode()
    while head:
        head_next = reversed_head.next              # head 다음 노드 (A) 임시 저장
        reversed_head.next = ListNode(head.val)     # 추가할 노드 (B) 생성하여 head의 다음 노드로 설정
        reversed_head.next.next = head_next         # B 노드 다음 A 노드가 오도록 연결
        head = head.next                            # 입력된 linked list의 next node
    return reversed_head.next                       # 첫 node는 dummy node

# recursive solution
# 220p

if __name__ == "__main__":
    linked_list = cur = ListNode()
    for val in [1, 2, 3, 4, 5]:
        cur.next = ListNode(val)
        cur = cur.next

    reversed = reverseList(linked_list.next)
    while reversed != None:
        print(reversed.val)
        reversed = reversed.next