class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 0:
        #     return 0
        # dp = [0 for _ in range(n)]
        # dp[0] = nums[0]
        # for i in range(1,n):
        #     if dp[i-1] > 0:
        #         dp[i] = dp[i-1] + nums[i]
        #     else:
        #         dp[i] = nums[i]
        # return max(dp)
        if len(nums) == 0:
            return 0
        pre = 0
        res = nums[0]
        for i in range(len(nums)):
            pre = max(nums[i], pre+nums[i])
            res = max(res, pre)
        return res
