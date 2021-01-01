"""
## 12-1. 섬의 개수

1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.
(연결되어 있는 1의 덩어리 개수를 구하라.)
"""
from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 136ms
        def dfs(i, j):
            # 인덱스가 grid를 넘어가거나, 값이 1이면 return
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#' # 방문 표시
            # 이웃 노드 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    print(grid)
                    count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ])) # 1
    print(sol.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ])) # 3