# 홀짝 연결 리스트
# 연결리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성해라.

def oddEvenList(head) :
    if head is None :
        return head

    odd, even,even_head = head, head.next, head.next

    while even and even.next : 
        odd.next , even.next = odd.next.next , even.next.next
        odd, even = odd.next , even.next

    odd.next = even_head
    return head 
