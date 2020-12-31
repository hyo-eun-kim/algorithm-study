"""
## 12-3. 순열

서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
"""
from typing import *
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 32ms
        return list(map(list, permutations(nums)))

    def permute2(self, nums: List[int]) -> List[List[int]]:
        # 36ms
        def dfs(elements, path):
            # 남은 요소가 없으면 백트래킹
            if not elements:
                result.append(path)
                return
            for i in range(len(elements)):
                dfs(elements[:i] + elements[i + 1:], path + [elements[i]])

        result = []
        dfs(nums, [])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    print(sol.permute2([1, 2, 3]))