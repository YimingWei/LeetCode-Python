class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1.一次遍历
        # n = len(prices)
        # minPrice = prices[0]
        # maxProfit = 0
        # for i in range(n):
        #     minPrice = min(minPrice, prices[i])
        #     maxProfit = max(maxProfit, prices[i]-minPrice)
        # return maxProfit

        # 2.动态规划
        n = len(prices)
        minPrice = prices[0]
        dp = [0] * n
        if n == 0:
            return 0
        for i in range(1,n):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minPrice)
        return dp[-1] 
