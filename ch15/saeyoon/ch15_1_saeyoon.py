"""
## 15-1. 배열의 K번째 큰 요소

정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
"""
import heapq
from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 60ms
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 64ms
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))