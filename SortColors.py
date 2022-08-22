class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 1.冒泡排序，双重for循环
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # 2.双指针，单循环
        zero = 0
        two = n
        i = 0
        while i < two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i+= 1
            else:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]                
