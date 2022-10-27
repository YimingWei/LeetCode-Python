class Solution:
    def countSubstrings(self, s: str) -> int:
        # 从下到上从左到右遍历
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    result += 1
                    dp[i][j] = True
        return result
