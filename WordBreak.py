class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n): # i表示s的索引
            for j in range(i+1, n+1): #dp[i]表示s里在索引i之前的字符串可以用wordDict里的单词表示
                if dp[i] and (s[i:j] in wordDict): #只需要确保s[i:j]这段字符在wordDict里可以表示
                    dp[j] = True
        return dp[-1]
