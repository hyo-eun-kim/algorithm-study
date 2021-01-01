class Solution:
    def dfs(self, grid: List[List[str]], i: int, j:int):
        # 유효한 범위를 벗어나거나 grid 내 해당 영역이 육지가 아니라면
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or\
            grid[i][j] != "1":
            return

        grid[i][j] = '0' # 탐색한 영역이라고 표시해줌
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        # 예외 처리
        if not grid:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': # 육지를 찾으면
                    self.dfs(grid,i,j) # 거기서부터 탐색 시작
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count
        
