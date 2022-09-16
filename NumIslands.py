class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(grid, row, col):
            if not 0<=row<m or not 0<=col<n: #越界
                return
            if grid[row][col] == "0": #已经是海水了
                return
            grid[row][col] = "0" #把这块陆地淹了,然后处理上下左右邻地
            dfs(grid, row-1, col)
            dfs(grid, row+1, col)
            dfs(grid, row, col-1)
            dfs(grid, row, col+1)
        
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(grid, i, j) # 淹没包含这块陆地的岛屿
        
        return res
