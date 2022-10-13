class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        l, r = 1, 1
        // l为当前数左边数的乘积，res先保存左边数乘积
        for i in range(n):
            res[i] *= l
            l *= nums[i]
        // r为当前数右边数的乘积，res保存左边数x右边数的结果
        for i in range(n-1, 0, -1):
            r *= nums[i]
            res[i-1] *= r //需要注意边界
        return res
