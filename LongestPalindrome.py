class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False]*n for _ in range(n)]
        # 当i=j, s[i]=s[j]
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n+1):
            for i in range(0, n):
                # 字串长度L=j-i+1
                j = L+i-1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 即L为2或3时
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    begin = i
        return s[begin:begin+max_len]

# 解法二：中心扩展法
# class Solution:
#   def expand(self, s, left, right):
#     while left>=0 and right<len(s) and s[left]==s[right]:
#       left -= 1
#       right += 1
#     return left+1, right-1

#   def longestPalindrome(self, s: str) -> str:
#     start, end = 0, 0
#     for i in range(len(s)):
#       # 中心有一个数
#       left1, right1 = self.expand(s, i, i)
#       # 中心没有数
#       left2, right2 = self.expand(s, i, i+1)
#       if right1-left1 > end-start:
#         start, end = left1, right1
#       if right2-left2 > end-start:
#         start, end = left2, right2
#     return s[start: end+1]
