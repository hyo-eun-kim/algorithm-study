'''
https://leetcode.com/problems/merge-two-sorted-lists/
정렬되어 있는 두 연결 리스트를 합쳐서 정렬된 연결 리스트를 만들어라
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 첫 답안
# 재귀보다는 살짝 빠르지만, 지저분하다 :(
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    # 이 부분도 불필요
    # merged를 return 하는 게 아니라, merged.next 리턴하면 해결될 문제 ..
    if l1 == None and l2 == None:
        return None

    merged = ListNode()  # (0, None)
    cur_node = merged
    l1_cur, l2_cur = l1, l2  # 불필요한 부분

    while (l1_cur != None) and (l2_cur != None):
        # l1_cur이나 l2_cur 중 하나가 None이 되면 while 탈출
        if l1_cur.val < l2_cur.val:
            cur_node.val, cur_node.next = l1_cur.val, ListNode()
            l1_cur = l1_cur.next
        else:
            cur_node.val, cur_node.next = l2_cur.val, ListNode()
            l2_cur = l2_cur.next
        cur_node = cur_node.next

    if l1_cur != None:
        # 이 부분 불필요 코드 축약 가능!
        while l1_cur.next != None :
            cur_node.val, cur_node.next = l1_cur.val, ListNode()
            cur_node = cur_node.next
            l1_cur = l1_cur.next
        cur_node.val = l1_cur.val
    if l2_cur != None:
        # 이 부분 불필요 코드 축약 가능!
        while l2_cur.next != None :
            cur_node.val, cur_node.next = l2_cur.val, ListNode()
            cur_node = cur_node.next
            l2_cur = l2_cur.next
        cur_node.val = l2_cur.val

    return merged


# 위의 답안을 개선한 답안
def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:

    merged = cur_node = ListNode() # (0, None)
    while l1 and l2:
        # print(f"l1 = {l1.val}, l2 = {l2.val}")
        if l1.val < l2.val:
            cur_node.next = l1
            l1 = l1.next
            cur_node = cur_node.next
        else:
            cur_node.next = l2
            l2 = l2.next
            cur_node = cur_node.next

    # 위에서는 나머지 부분을 이어붙였는데, 그럴 필요가 없다!
    # 그냥 l1, l2 대입해주면 linked list 이므로 따라온다
    # if l1 != None:
    #     cur_node.next = l1
    # else:
    #     cur_node.next = l2

    cur_node = l1 or l2
    # l1이 None이 아니면 l1이 리턴
    # l1이 None이면 l2가 리턴
    return merged.next


def recursive_solution(l1: ListNode, l2: ListNode) -> ListNode:
    


if __name__ == "__main__":
    A_node_cur = A_node =  ListNode()
    for val in [1, 2, 3, 4, 5]:
        A_node_cur.next = ListNode(val)
        A_node_cur = A_node_cur.next

    B_node_cur = B_node = ListNode()
    for val in [1, 2, 10, 11, 12]:
        B_node_cur.next = ListNode(val)
        B_node_cur = B_node_cur.next

    merged = mergeTwoLists2(A_node.next, B_node.next)
    while merged != None:
        print(merged.val)
        merged = merged.next