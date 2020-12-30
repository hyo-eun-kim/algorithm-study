"""
## 12-5. 조합의 합

숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라.
각 원소는 중복으로 나열 가능하다.
"""
from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 76ms
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        result = []
        dfs(target, 0, [])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))