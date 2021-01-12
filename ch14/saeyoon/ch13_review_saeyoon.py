"""
## 타겟 넘버

N개의 마을로 이루어진 나라가 있습니다.
이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다.
각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다.
도로를 지날 때 걸리는 시간은 도로별로 다릅니다.
현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다.
각 마을로부터 음식 주문을 받으려고 하는데,
N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.

다음은 N = 5, K = 3인 경우의 예시입니다.

그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 3 이하의 시간에 배달할 수 있습니다.
그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다.
따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.

마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.
"""
from collections import defaultdict
import heapq


def solution(N, road, K):
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = {node: float('inf') for node in range(1, N+1)}
    dist[1] = 0

    queue = []
    heapq.heappush(queue, [dist[1], 1])

    while queue:
        d, node = heapq.heappop(queue)
        if dist[node] < d:
            continue
        for adjacent, d2 in graph[node]:
            distance = d + d2
            if distance < dist[adjacent]:
                dist[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return sum(1 if i <= K else 0 for i in dist.values())


if __name__ == '__main__':
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)) # 4
    print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)) # 4
