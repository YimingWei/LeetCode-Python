class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid-1 >= 0 and nums[mid-1] == target:
                    return [mid-1, mid]
                elif mid+1 <= len(nums)-1 and nums[mid+1] == target:
                    return [mid, mid+1]
                else:
                    return [mid, mid]
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return [-1, -1]
