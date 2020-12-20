'''
https://leetcode.com/problems/design-hashmap/

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
'''


# 204ms (faster than 81.74%)
# 17.5MB (less than 43.44%)

class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 길이가 1,000,000인 배열을 만드는 것이 아니라 1,000인 배열을 만들어서 해결해보자!
        self.map_size = 2
        self.map = [None for _ in range(self.map_size)]


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # hash function을 통과한 값 (modulo-division method)
        key_value = key % self.map_size

        if self.map[key_value] is None:
            self.map[key_value] = Node(key, value)
        else:
            cur_node = self.map[key_value]
            while cur_node:
                if cur_node.key == key:
                    # 동일한 key를 가진 node를 발견했다면 value 수정
                    cur_node.value = value
                    return
                if cur_node.next is None: break
                cur_node = cur_node.next
            # 동일한 key를 가진 node를 발견하지 못했다면 추가
            cur_node.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # hash function 통과
        key_value = key % self.map_size

        if self.map[key_value] is None:
            return -1
        else:
            cur_node = self.map[key_value]
            while cur_node:
                if cur_node.key == key:
                    return cur_node.value
                cur_node = cur_node.next
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # hash function 통과
        key_value = key % self.map_size

        if self.map[key_value] is None:
            return
        else:
            before_node = self.map[key_value]
            cur_node = before_node.next
            if before_node.key == key:
                self.map[key_value] = cur_node
                return

            while cur_node:
                if cur_node.key == key:
                    before_node.next = cur_node.next
                    return
                before_node = before_node.next
                cur_node = cur_node.next



if __name__ == "__main__":
    my_hash = MyHashMap()
    my_hash.put(1, 1)
    my_hash.put(2, 2)
    my_hash.put(3, 3)
    my_hash.put(4, 1)
    my_hash.put(5, 2)
    my_hash.put(6, 3)
    my_hash.put(2, 1)
    my_hash.remove(2)

    print(my_hash.get(1))  # 1
    print(my_hash.get(2))  # -1
    print(my_hash.get(3))  # 3
    print(my_hash.get(4))  # 1
    print(my_hash.get(5))  # 2
    print(my_hash.get(6))  # 3


