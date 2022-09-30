class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1.内置函数sort
        # nums.sort()
        # return(nums[len(nums)-k])
        # 2.手写快排改进版
        index = randint(0, len(nums)-1)
        pivot = nums[index]
        less_part = [n for n in nums if n < pivot]
        great_part = [n for n in nums if n >= pivot]
        if len(great_part) == k-1:
            return pivot
        elif len(great_part) > k-1:
            return self.findKthLargest(great_part, k)
        else:
            return self.findKthLargest(less_part, k-len(less_part)-1)
