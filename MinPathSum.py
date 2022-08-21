class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) #行数
        n = len(grid[0]) #列数
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n): #dp[i][i]表示到grid[i][j]的最小路径的值
        #         if i == 0 and j == 0: #grid[i][j]在左边界和上边界
        #             dp[i][j] = grid[i][j]
        #         elif i == 0 and j > 0: #grid[i][j]在上边界
        #             dp[i][j] = dp[i][j-1] + grid[i][j]
        #         elif i > 0 and j == 0: #grid[i][j]在左边界
        #             dp[i][j] = dp[i-1][j] + grid[i][j]
        #         elif i > 0 and j > 0: #grid[i][j]不在左边界也不在上边界
        #             dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        # return dp[i][j]
        # 也可以直接修改原矩阵，节省内存
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
        return grid[i][j]
