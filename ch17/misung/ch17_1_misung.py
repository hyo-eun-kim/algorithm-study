# 연결리스트를 nlog(n) 에 정렬하라.
# 병합 정렬을 이용해보자 => divide conquer
# 연결리스트의 경우, 어디까지 왔는지 (어디가 중간인지) 알수가 없기때문에 "런너" 기법을 사용해보자!


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeLists(self, l1, l2):
#         if l1 and l2:
#             if l1.val > l2.val: # 값을 비교해서 swap 
#                 l1,l2= l2, l1
#             l1.next =self.mergeLists(l1.next,l2)  

#         return l1 or l2  # l1이 있으면 l1 리턴, l1이 없으면 l2 리턴 

#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not (head and head.next):
#             return head

#     half, slow, fast = None, head, head   
#     while fast and fast.next :  # fast 가 끝에 도달할때까지 반복
#         half, slow, fast = slow, slow.next, slow.next.next   #slow 는 한칸씩, fast 는 두칸씩 이동한다, half 는 slow의 바로 이전값. 
#     half.next = None  # half 의 위치를 기준으로 연결리스트의 관계를 끊어버림. 

#     l1 =self.sortList(head)  # 시작노드
#     l2 = self.sortList(slow) # 중간노드

#     return self.mergeLists(l1,l2) # 쪼갠 아이템을 다시 합친다.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
     def sortList(self, head):
        p = head
        mylist=[]

        while p :
            mylist.append(p.val)
            p = p.next
    
        mylist.sort()

        p=head
        for i in range(len(mylist)):
            p.val=mylist[i]
            p=p.next
        return head