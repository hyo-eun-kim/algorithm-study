'''
https://leetcode.com/problems/odd-even-linked-list/
연결 리스트를 홀수 노드 디음에 짝수 노드가 오도록 재구성하라.
(여기서 홀수 노드, 짝수 노드는 node안의 val이 아니라, node의 number)
공간 복잡도 0(1), 시간복잡도 o(n) 에 풀이하라.

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: ListNode) -> ListNode:
    if head is None:
        return None

    odd_node = head
    even_node = first_even_node = head.next
    while even_node and even_node.next:
        # even_node가 None이거나 even_node.next가 None이면 break
        # even_node의 다음 노드를 odd_node의 next로
        # even_node의 다다음 노드를 even_node의 next로
        odd_node.next, even_node.next = even_node.next, even_node.next.next
        odd_node = odd_node.next
        even_node = even_node.next

    odd_node.next = first_even_node
    return head


if __name__ == "__main__":
    head = cur = ListNode()
    for val in [2, 1, 3]:
        cur.next = ListNode(val)
        cur = cur.next

    oddEven = oddEvenList(head.next)
    while oddEven:
        print(oddEven.val)
        oddEven = oddEven.next

