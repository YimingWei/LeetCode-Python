import operator
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # 先排序
        for i in range(n):
            intervals.sort(key=operator.itemgetter(0))
        rm = []
        for i in range(n-1):
            current_end = intervals[i][1]
            post_start = intervals[i+1][0]
            if current_end >= post_start:
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                rm.append(i)
        res = []
        for i in range(n):
            if i not in rm:
                 res.append(intervals[i])
        return res
