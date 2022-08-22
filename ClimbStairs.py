class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 2
            elif i >= 2:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
