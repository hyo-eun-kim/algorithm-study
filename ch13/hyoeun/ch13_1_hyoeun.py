'''
https://leetcode.com/problems/network-delay-time/ (leetcode 743)

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

N will be in the range [1, 100].    = number of nodes
K will be in the range [1, N].      = start node
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
    - u : source
    - v : target
    - w : time
'''
from typing import List
import heapq
from collections import defaultdict

# 496ms (faster than 41%)
# 16.4MB (less than 27%)
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        from_to = defaultdict(list)
        for u, v, w in times:
            from_to[u].append((v, w))

        heap = []
        visited = {}
        heapq.heappush(heap, (0, K))  # distance, node
        while heap:
            dist, node = heapq.heappop(heap)
            if node not in visited:
                visited[node] = dist
                for v, w in from_to[node]:
                    heapq.heappush(heap, (dist+w, v))

        if len(visited) == N:
            return max(visited.values())
        else:
            return -1


if __name__ == "__main__":
    times = [[1, 2, 1]]
    N = 2
    K = 2

    solution = Solution()
    print( solution.networkDelayTime(times, N, K) )





