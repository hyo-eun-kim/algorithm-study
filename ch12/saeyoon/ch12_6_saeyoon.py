"""
## 12-6. 부분 집합

모든 부분 집합을 리턴하라
"""
from typing import *
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 36ms
        result = []
        for i in range(len(nums) + 1):
            result.extend(list(map(list, combinations(nums, i))))
        return result

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # 36ms
        def dfs(elements, path):
            result.append(path)

            for i in range(len(elements)):
                dfs(elements[i + 1:], path + [elements[i]])

        result = []
        dfs(nums, [])
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets2([1, 2, 3]))