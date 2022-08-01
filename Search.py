class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            # target的值等于nums[mid]，说明已找到下标，即为mid
            if nums[mid] == target:
                return mid
            # 总共4种情况：首先，如果nums[left] <= nums[mid]，则说明左半边是有序的
            # 进一步假设（1）target在左边区间，则右半边舍弃，右边界right = mid-1
            # （此处“-1”是因为上一步不满足nums[mid] == target），然后在左半边继续找
            # target的位置；（2）左半边有序，target在右半边，同理；（3）右半边有序，
            # target在右半边，同理；（4）右半边有序，target在左半边，同理
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
