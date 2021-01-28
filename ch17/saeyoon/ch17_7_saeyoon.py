"""
## 17-7. 원점에 K번째로 가까운 점

평면상에 points 목록이 있을 때,
원점 (0, 0)에서 K번 가까운 점 목록을 순서대로 출력하라.
평면상 두 점의 거리는 유클리드 거리로 한다.
"""
from typing import *
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 636ms
        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        return points[:K]

    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 712ms
        heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (dist, [point[0], point[1]]))

        result = []
        for _ in range(K):
            result.append(heapq.heappop(heap)[1])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1))
    print(sol.kClosest2([[3, 3], [5, -1], [-2, 4]], 2))
