"""
## 캐시
"""
from typing import *
from collections import deque


def solution(cacheSize: int, cities: List[str]) -> int:
    time = 0
    cache = deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower() # 대소문자 구분 X

        # cache hit
        if c in cache:
            cache.remove(c)
            cache.append(c)
            time += 1
        # cache miss
        else:
            cache.append(c)
            time += 5

    return time


if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                       "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))