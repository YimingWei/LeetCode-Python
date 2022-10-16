class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. 二分法
        # left = 1
        # right = len(nums) - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     count = 0
        #     for num in nums:
        #         if num <= mid:
        #             count += 1
        #     if count <= mid:
        #         left = mid + 1
        #     if count > mid:
        #         right = mid
        # return left
        # 2. 快慢指针
        slow, fast = 0, 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        find = 0
        while 1:
            find = nums[find]
            slow = nums[slow]
            if find == slow:
                return find
