class Solution:
    def numSquares(self, n: int) -> int:
        res = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                res[i] = min(res[i], res[i - j * j] + 1)
                j += 1
        return res[n]
