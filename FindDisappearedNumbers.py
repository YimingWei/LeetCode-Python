class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1.空间O(n)
        # n = len(nums)
        # s = set(nums)
        # res = []
        # for i in range(1, n+1):
        #     if i not in s:
        #         res.append(i)
        # return res
        # 2.空间O(1)
        n = len(nums)
        res = []
        for i in range(n):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
