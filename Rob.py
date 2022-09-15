class Solution:
    def rob(self, nums: List[int]) -> int:
        """ 
            f(k)表示偷前k间房子所能获取的最大金额
            f(k)的取值有两种方案:
            一是第k间房子不偷,取前k-1间房子的最大金额f(k-1)
            二是第k间房子偷,取前k-2间房子的最大金额再加上第k间房子的金额,即f(k-2)+nums[k-1]
            f(k) = max(f(k-1), f(k-2)+nums[k-1])
            f(0)=0, f(1)=nums[0]
        """
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[-1]
