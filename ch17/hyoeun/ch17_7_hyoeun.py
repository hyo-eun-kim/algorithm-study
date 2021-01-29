'''
64. 원점에 K번째로 가까운 점
평면상에 points 목록이 있을 때 원점 (0, 0)에서 K번째로 가까운 점 목록을 순서대로 출력
평면상 두 점의 거리를 유클리드 거리로 한다.
'''
import heapq
from typing import List

# heap 정렬 이용한 문제
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            heapq.heappush(heap, (x * x + y * y, (x, y)))

        ret = []
        for _ in range(K):
            ret.append(heapq.heappop(heap)[1])
        return ret