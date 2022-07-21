class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        # 如果nums为空或者元素不足3个，则返回空
        if not nums or n < 3:
            return res
        # 对数组排序
        nums.sort()
        for i in range(n):
            # 因为数据已排序，如果三元组中第一个元素i的值大于0，则不可能有三元组和为0
            if nums[i] > 0:
                return res
            # 排除第一个元素i相同的情况，避免重复计算
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 左指针
            L = i + 1
            # 右指针
            R = n - 1
            while L < R:
                # 若三元组和为0
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 如果L的下一个元素和L相同，则向右移一位，避免重复计算
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    # 如果R的左边一个元素和R相同，则向左移一位，避免重复计算
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    # 将L、R赋值为恰好不满足while循环条件时的值
                    L += 1
                    R -= 1
                # 和大于0说明太大了，将R向左移一位，使和变小
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                # 和小于0说明太小了，将L向右移一位，使和变大
                else:
                    L += 1
        return res
