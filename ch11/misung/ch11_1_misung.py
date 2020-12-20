# 해시 맵 디자인
import collections

class ListNode:
    def __init__(self,key=None,value=None):
        """
        Initialize your data structure here.
        """
        self.key = key
        self.value = value
        self.next =  None


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size =1000  # 기본 사이즈 1000개로 설정
        self.table = collections.defaultdict(ListNode)  # 


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key%self.size
        if self.table[index].value is None:  # 해당 인덱스의 해시테이블이 비어있으면  + 여기서 값으로 비교한 이유는 defaultdict 를 사용했기때문!
            self.table[index]=ListNode(key,value)  # 바로 삽입
            return

        # 해당 인덱스에 노드가 존재하는 경우
        p= self.table[index]  # 인덱스의 첫번째 값
        while p :
            if p.key == key: # 이미 키가 존재 할 경우 업데이트 하고 빠져나간다.
                p.value = value
                return 
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)  # 새 노드 연결

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key%self.size
        if self.table[index].value is None : # 아직 어떤한 키도 이 값으로 해싱되지 않은 경우
            return -1

        # 노드가 존재하면 key 탐색
        p = self.table[index]
        while p : 
            if p.key == key:
                return p.value
            p=p.next  # 일치하는 키를 찾을때 까지 next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key%self.size
        if self.table[index].value is None :  # 인덱스에 노드가 없을때,
            return 
        
        p= self.table[index]
        if p.key ==key:  # 첫번째 노드일때 삭제
            self.table[index] = ListNode() if p.next is None else p.next  # p.next 가 없으면 아예 빈 노드로! 있으면 이어주고!
            return

        # 연결리스트 노드 삭제
        prev = p
        while p :
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next # 이전노드의 다음을 현재 노드의 다음으로 연결한다!

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)