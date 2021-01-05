"""
## 13-1. 네트워크 딜레이 타임

K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
불가농할 경우 -1을 리턴한다.
입력값 (u, v, w)는 각각 출발지，도착지, 소요시간으로 구성되며，전체 노드의 개수는 N으로 입력받는다.
"""
from typing import *
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 436ms
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N + 1)}
        dist[K] = 0

        queue = []
        heapq.heappush(queue, [dist[K], K])

        while queue:
            d, node = heapq.heappop(queue)
            if dist[node] < d:
                continue
            for adjacent, d2 in graph[node]:
                distance = d + d2
                if distance < dist[adjacent]:
                    dist[adjacent] = distance
                    heapq.heappush(queue, [distance, adjacent])

        return max(dist.values()) if max(dist.values()) <= 100 else -1

    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        # 452ms
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}

        queue = []
        heapq.heappush(queue, [0, K])

        while queue:
            d, node = heapq.heappop(queue)
            if node in dist:
                continue
            dist[node] = d
            for adjacent, d2 in graph[node]:
                distance = d + d2
                if adjacent not in dist:
                    heapq.heappush(queue, [distance, adjacent])

        return max(dist.values()) if len(dist) == N else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(sol.networkDelayTime2([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))