class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1.dp
        # n = len(nums)
        # dp = [1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        # 2.binary search
        n = len(nums)
        d = []
        for num in nums:
            index = bisect_left(d, num)
            if index == len(d):
                d.append(num)
            else:
                d[index] = num
        return len(d)
