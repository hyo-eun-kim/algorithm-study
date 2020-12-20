'''
28. 해시맵 디자인

다음의 기능을 제공하는 해시맵을 디자인하라.

* put(key, value): 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이
트한다.
* get(key): 키에 해당하는 값을 조회 한다. 만약 키가 존재하지 않는다면 -1을 리
턴한다
* remove(key): 키에 해당하는 키, 값을 해시맵에서 삭제한다.

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2) ;
hashMap.get(1) ;     // 1을 리턴한다
hashMap.get(3) ;     // -1을 리턴한다(키가존재하지 않음)
hashMap.put(2, 1) ;  // 값을업데이트한다
hashMap.get(2);      // 1을리턴한다
hashMap.remove(2) ;  // 키 2 에 해당하는 키 , 값을 삭제한다
hashMap.get(2) ;     // - 1을 리턴한다(키가삭제되어 존재하지 않음)
'''

# 체이닝을 이용한 풀이
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우(해시 충돌 발생)
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        # 노드가 존재하지 않을 때
        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next # p안에 있는 모든 노드를 훑어본다.
        return -1 # 결국 없으면 -1 출력

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        # 노드가 존재하지 않을 때
        if self.table[index].value is None:
            return 
        
        # 인덱스의 첫 번째 노드일 때 삭제
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
            
    # 232 ms


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)