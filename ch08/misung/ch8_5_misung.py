# 페어의 노드스왑
# 연결리스트를 입력받아 페어단위로 스왑하라

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = head

    while cur and cur.next : 
        cur, cur.next = cur.next.val , cur.val
        cur = cur.next.next

    return head  # 왜 head를 return 해야하는가? cur과 처음에 같은걸 참조하면서 cur로 값을 바꾸면서 와서,,  cur -> none 