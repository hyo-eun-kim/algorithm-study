# 역순 연결리스트
# 인덱스 m 에서 n까지를 역순으로 만들어라.
# 인덱스 m 은 1부터 시작한다.

def reverseBetween(head, m, n):
    if not head : 
        return None

    list_node =[]
    node = head
    while node :
        list_node.append(node.val)
        node = node.next

    # 뒤집고 
    rev = list_node[:m-1] + list_node[m-1:n][::-1] + list_node[n:]

    # 리스트를 연결리스트로
    my_head = ListNode(rev[0])
    rev_node = my_head
    for i in rev[1:]:
        rev_node.next =ListNode(i)
        rev_node = rev_node.next
    return my_head