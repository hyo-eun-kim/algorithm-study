'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/
시작점에서 도착점까지의 가장 저렴한 가격을 계산하되，
K개의 경유지 이내에 도착하는 가격을 리턴하라.
경로가 존재하지 않을 경우 -1을 리턴한다 .
'''
from typing import List
from collections import defaultdict
import heapq

# 104ms (faster than 42%)
# 15.4MB (67.55%)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from_to = defaultdict(list) # key: from, value: to, dist
        for u, v, w in flights:
            from_to[u].append((v, w))

        heap = []
        visited = {}
        # complete = [] 필요없다
        heapq.heappush(heap, (0, 0, src))   # dist, n-th, node
        while heap:
            dist, n_th, node = heapq.heappop(heap)
            if node == dst:
                # 도착지 도달! -> 이렇게 할 필요 X
                # complete.append(dist)
                # continue
                return dist
            if n_th == K+1:
                # 도착지에 도달하지 못했지만 경유지 수 제한으로 더 탐색할 수 없는 경우
                continue
            if node not in visited or visited[node] > n_th:
                # 경유지 도달도 못 했고, 더 탐색할 수 있는 기회가 있는 경우
                visited[node] = n_th  # time exceeded 방지
                for v, w in from_to[node]:
                    if v not in visited or visited[v] > n_th+1:
                        heapq.heappush(heap, (dist + w, n_th + 1, v))  # dist, n-th, node

        return -1
        # if not complete:
        #     return -1
        # return min(complete)

# 책 속의 해설
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        k = 0   # 경유 횟수
        Q = [(0, src, k)]  # (dist, src)

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k <= K:
                k += 1
                for v, w in graph[node]:
                    alt = price+w
                    heapq.heappush(Q, (alt, v, k))

        return -1

if __name__ == "__main__":
    n = 5
    edges = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    src = 0
    dst = 2
    k = 2

    solution = Solution()
    print(solution.findCheapestPrice(n, edges, src, dst, k))

    n = 3
    edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    print(solution.findCheapestPrice(n, edges, src, dst, k))