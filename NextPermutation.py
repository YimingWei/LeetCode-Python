class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(low, high):
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                # 完成高位与最接近且大于它的低位进行交换, 
                # 最接近的低位，一定是逆序遍历大于它的第一个数
                for j in range(n-1, 0, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                # 再将高位往后的低位进行逆序，即从小到大排列
                reverse(i, n-1)
                break
        # 正常循环结束，则说明是最大的，直接反转
        else:
            reverse(0, n-1)
