class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rowNum = len(grid)
        colNum = len(grid[0])

        island = 0

        def dfs(row,col):
            if row<0 or row>= rowNum:
                return
            if col<0 or col>=colNum:
                return

            ## 값이 1이면 x로 바꾼다.
            if grid[row][col] == "1":
                grid[row][col] = "x"   
            else:
                return

            ## 인접한 점을 보고 이 점에 대해서도 진행
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            return

        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i, j)


        return island  
