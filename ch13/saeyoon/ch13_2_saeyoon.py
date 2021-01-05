"""
## 13-2. K 경유지 내 가장 저렴한 항공권

시작점에서 도착점까지의 가장 저렴한 가격을 계산하되,
K개의 경유지 이내에 도착하는 가격을 리턴하라.
경로가 존재하지 않을 경우 -1을 리턴한다.
"""
from typing import *
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 88ms
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = []
        heapq.heappush(queue, [0, src, K])

        while queue:
            price, node, k = heapq.heappop(queue)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    distance = price + w
                    heapq.heappush(queue, [distance, v, k-1])

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
    print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 200], [0, 2, 500]], 0, 2, 0))