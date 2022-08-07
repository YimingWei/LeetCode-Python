class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, nums):
            if not nums:
                res.append(path[:])
            for i in range(len(nums)):
                path.append(nums[i])
                # 回传nums中去除nums[i]后的列表
                backtrack(path, nums[:i]+nums[i+1:])
                path.pop()
        backtrack([],nums)
        return res
