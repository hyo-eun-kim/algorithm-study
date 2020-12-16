"""
## 11-1. 해시맵 디자인

다음 기능을 제공하는 해시맵을 디자인하라.

- put(key, value): 키, 값을 해시맵에 삽입, 이미 존재하는 키라면 업데이트
- get(key): 키에 해당하는 값을 조회, 만약 키가 존재하지 않는다면 -1 리턴
- remove(key): 키에 해당하는 키, 값을 해시맵에서 삭제
"""
from typing import *
from collections import defaultdict


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없으면 바로 삽입
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트로 처리
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
        index = key % self.size
        # 인덱스에 노드가 없으면 -1 반환
        if self.table[index].value is None:
            return -1

        # 노드가 존재하면 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없으면 -1 반환
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
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


if __name__ == '__main__':
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    print(hashmap.get(1)) # 1
    print(hashmap.get(3)) # -1
    hashmap.put(2, 1)
    print(hashmap.get(2)) # 1
    hashmap.remove(2)
    print(hashmap.get(2)) # -1