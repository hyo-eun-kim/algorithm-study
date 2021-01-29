'''
HEAP
https://programmers.co.kr/learn/courses/30/lessons/42626
'''

from collections import deque
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    N = len(scoville)
    count = 0
    # 최악의 경우를 생각하자!
    for _ in range(N - 1):
        scov1 = heapq.heappop(scoville)
        scov2 = heapq.heappop(scoville)
        if scov1 >= K:
            return count
        heapq.heappush(scoville, scov1 + 2 * scov2)
        count += 1

    return count if heapq.heappop(scoville) >= K else -1


def solution2(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        scov1 = heapq.heappop(scoville)
        if scov1 >= K:
            return count
        if not scoville:
            return -1
        scov2 = heapq.heappop(scoville)
        heapq.heappush(scoville, scov1 + 2 * scov2)
        count += 1
    return -1