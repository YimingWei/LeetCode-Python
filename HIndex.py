class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations)
        #遍历，时间复杂度为n
        def can(mid):
            tmp = 0
            for citation in citations:
                if citation >= mid:
                    tmp += 1
            return tmp
        #二分查找，时间复杂度为logn
        while l <= r:
            mid = (l + r) // 2
            if can(mid) >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r
        #总的时间复杂度为nlogn
