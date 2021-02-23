"""
## 21-2. 키에 따른 대기열 재구성

여러 명의 사람들이 줄을 서 있다.
각각의 사람은 (h, k)의 두 정수 쌍을 갖는데,
h는 그 사람의 키, k는 앞에 줄 서 있는 사람들 중 자신으 키 이상인 사람들의 수를 뜻한다.
이 값이 올바르도록 줄을 재정렬하는 알고리즘을 작성하라.
"""
from typing import *
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 96ms
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []
        for person in people:
            result.insert(person[1], person)
        return result


    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        # 100ms
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(sol.reconstructQueue2([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))