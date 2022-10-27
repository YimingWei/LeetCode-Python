class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 小根堆
        n = len(nums)
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        l = dic.values() #各个数字出现的频率序列

        def findKthLargest(sequence, k):
            heap = []
            for item in sequence:
                heapq.heappush(heap, -item)
            for i in range(k-1):
                heapq.heappop(heap)
            return -heap[0] #第k大的频率
        
        kth = findKthLargest(l, k)
        res = []
        for k, v in dic.items():
            if v >= kth:
                res.append(k) #题目中只需要给出前k个高频元素的集合，并不需要对结果排序
        return res
