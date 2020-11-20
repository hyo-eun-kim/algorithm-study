# 두수의 덧셈
# 두 수의 덧셈
# 역순으로 저장된 연결 리스트의 숫자를 더하라

def addTwoNumbers(l1, l2):
    list1 = []
    list2 = []

    # 연결리스트를 파이썬 리스트로 변환
    while l1 is not None : # None : 값 자체가 정의되어있지 않다. is로만 비교 가능 
        list1.append(l1.val)
        l1 = l1.next
    while l2 is not None:
        list2.append(l2.val)
        l2 = l2.next

    # 뒤집어서 숫자로 바꿔서 더해줌
    sumNum = int("".join(str(e) for e in list1[::-1])) + int("".join(str(e) for e in list2[::-1]))

    # 다시 뒤집어서 리스트로 만들어줌
    #res = [int(x) for x in str(sumNum)[::-1]]

    # 리스트를 뒤집에서 연결리스트로
    prev=None
    for r in str(sumNum):
        node = ListNode(r)
        node.next = prev
        prev = node
    return node