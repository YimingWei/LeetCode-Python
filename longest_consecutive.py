class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        for num in nums_set:
            if num-1 not in nums_set:
                tmp_num = num
                tmp_len = 1
                while tmp_num+1 in nums_set:
                    tmp_num += 1
                    tmp_len += 1
                length = max(length, tmp_len)
        return length