'''
https://leetcode.com/problems/number-of-islands/
1을 육지로, 0을 물로 가정한 2D grid map이 주어졌을 때, 섬의 개수를 계산하라.
'''
from typing import *
from collections import deque

# my solution
# faster than 94.67% (124ms)
# less than 94.07% (15MB) -> 클래스 변수 사용하기 15.4MB 사용 (less than 52.28%)
# BFS를 이용한 풀이
class Solution:
    # 클래스 멤버변수 선언
    grid: List[List[str]]  
    n_row: int
    n_col: int

    def BFS(self, start_i, start_j):
        queue = deque()
        queue.append((start_i, start_j))
        while queue:
            i, j = queue.popleft()
            self.grid[i][j] = '0'
            # 현재 위치에서 상하좌우 탐색해서 갈 수 있는 위치를 queue에 insert
            if i-1 >= 0 and self.grid[i-1][j] == '1' and (i-1, j) not in queue:
                queue.append((i-1, j))  # up
            if i+1 < self.n_row and self.grid[i+1][j] == '1' and (i+1, j) not in queue:
                queue.append((i+1, j))  # down
            if j-1 >= 0 and self.grid[i][j-1] == '1' and (i, j-1) not in queue:
                queue.append((i, j-1))  # left
            if j+1 < self.n_col and self.grid[i][j+1] == '1' and (i, j+1) not in queue:
                queue.append((i, j+1))  # right

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n_row, self.n_col = len(grid), len(grid[0])
        n_island = 0
        for i in range(self.n_row):
            for j in range(self.n_col):
                if self.grid[i][j] == '1':
                    n_island += 1
                    self.BFS(i, j)
        return n_island


# DFS를 재귀로 구현한 것을 이용
# faster than 76% (136ms)
# less than 52% (15.4MB)
class Solution2:
    grid: List[List[str]]  # class member 변수
    n_row: int
    n_col: int

    def dfs(self, i, j):
        if i < 0 or i >= self.n_row or j < 0 or j >= self.n_col or self.grid[i][j] == '0':
            return

        self.grid[i][j] = '0'
        self.dfs(i-1, j)  # down
        self.dfs(i+1, j)  # up
        self.dfs(i, j-1)  # left
        self.dfs(i, j+1)  # right

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n_row, self.n_col = len(grid), len(grid[0])
        n_island = 0
        for i in range(self.n_row):
            for j in range(self.n_col):
                if grid[i][j] == '1':
                    self.dfs(i, j)
                    n_island += 1
        return n_island


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    solution = Solution()
    print(solution.numIslands(grid))  # 3

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    solution2 = Solution2()
    print(solution2.numIslands(grid))  # 3
