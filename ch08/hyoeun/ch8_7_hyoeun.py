'''
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/
인덱스 m에서 n까지를 역순으로 만들어라.
인덱스 m은 1부터 시작한다

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if head is None:
        return None
    dummy_head = ListNode()
    dummy_head.next = head

    # m-1 index의 노드에 도착
    cur = dummy_head
    for i in range(m - 1):
        cur = cur.next

    first_node = cur.next
    last_node = cur.next.next
    for i in range(n - m):
        cur.next, last_node, cur.next.next = last_node, last_node.next, cur.next
    first_node.next = last_node
    return dummy_head.next


if __name__ == "__main__":
    head = cur = ListNode()
    for val in [1, 2, 3, 4, 5]:
        cur.next = ListNode(val)
        cur = cur.next

    new_head = reverseBetween(head.next, 2, 4)
    while new_head:
        print(new_head.val)  # 1, 4, 3, 2, 5
        new_head = new_head.next