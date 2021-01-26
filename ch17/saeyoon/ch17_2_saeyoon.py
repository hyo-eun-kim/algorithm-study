"""
## 17-2. 구간 병합

겹치는 구간을 병합하라.
"""
from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))