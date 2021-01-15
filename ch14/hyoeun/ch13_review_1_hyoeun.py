'''
https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3
다익스트라 알고리즘 문제
'''

from collections import defaultdict
import heapq


def solution(N, road, K):
    from_to = defaultdict(list)
    for a, b, c in road:
        from_to[a].append((b, c))
        from_to[b].append((a, c))

    min_dist = {}
    start = [(0, 1)]
    while start:
        dist, src = heapq.heappop(start)
        if src not in min_dist:
            min_dist[src] = dist
            while from_to[src]:
                trg, d = from_to[src].pop()
                heapq.heappush(start, (dist + d, trg))

    answer = sum([True if dist <= K else False for src, dist in min_dist.items()])
    return answer

