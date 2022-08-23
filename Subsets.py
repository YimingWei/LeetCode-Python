class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # 1.迭代法
        # res = [[]]
        # for item in nums:
        #     res = res + [[item] + num for num in res]
        # return res
        # 2.回溯法
        res = []
        path = []
        n = len(nums)
        def backtrace(nums, i):
            res.append(path[:])
            for j in range(i, n):
                path.append(nums[j])
                backtrace(nums, j+1)
                path.pop()
        
        backtrace(nums, 0)
        return res
