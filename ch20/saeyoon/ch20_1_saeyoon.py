"""
## 20-1. 최대 슬라이딩 윈도우

배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서
최대 슬라이딩 윈도우를 구하라라
"""
from typing import *
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []

        for i, n in enumerate(nums):
            while window and nums[window[-1]] <= n:
                window.pop()

            window.append(i)

            if i - window[0] >= k:
                window.popleft()

            if i + 1 >= k:
                result.append(nums[window[0]])

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(sol.maxSlidingWindow([1, -1], 1))
    print(sol.maxSlidingWindow([9, 11], 2))
    print(sol.maxSlidingWindow([4, -2], 2))