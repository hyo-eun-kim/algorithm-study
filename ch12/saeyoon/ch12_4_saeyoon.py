"""
## 12-4. 조합

전체 수 n을 입력받아 k개의 조합을 리턴하라.
"""
from typing import *
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 64ms
        return list(map(list, combinations(range(1, n+1), k)))

    def combine2(self, n: int, k: int) -> List[List[int]]:
        # 580ms
        def dfs(elements, k, index, path):
            if k == 0:
                result.append(path)
                return
            for i in range(index, len(elements)):
                dfs(elements, k-1, i+1, path + [elements[i]])

        result = []
        dfs(range(1, n+1), k, 0, [])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4, 2))
    print(sol.combine2(4, 2))