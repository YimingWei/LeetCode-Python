class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. hashmap(空间复杂度：O(n)，时间复杂度：O(n))
        # n = len(nums)
        # hashmap = {}
        # for i in range(n):
        #     if nums[i] not in hashmap:
        #         hashmap[nums[i]] = 1
        #     else:
        #         hashmap[nums[i]] += 1
        # for key in hashmap:
        #     if hashmap[key] > n/2: #因为所求的数在列表中必然只存在一个
        #         return key
        # 2. sort(空间复杂度：O(1)，时间复杂度：O(n))
        return sorted(nums)[len(nums)//2] #先排序；若n是奇数，则取的是中间的数；若n是偶数，则取的中间往右一个的数
