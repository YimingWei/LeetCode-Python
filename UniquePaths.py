class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # 1.组合数学
        # return math.comb(m+n-2, m-1)
        # 2.动态规划
        dp = [[0 for _ in range(n)] for _ in range(m)] #dp[i][j]表示到达[i][j]位置的路径数目
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0: #当前位置在左边界或上边界，则只能从dp[i-1][j]向下走一步或者从dp[i][j-1]向右走一步到达当前位置，因此只有一种路径
                    dp[i][j] = 1
                else: #当前位置不在边界上，则到达[i][j]只可能是从[i-1][j]或[i][j-1]位置走过来的，可以分解为到达[i-1][j]位置的路径数目与到达[i][j-1]位置的路径数目的和，因为到达这俩位置的路径不可能重复，所以数目可以直接相加
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
