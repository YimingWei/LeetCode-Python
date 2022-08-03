class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrace(candidates, path, target, start):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrace(candidates, path, target, i)
                path.pop()
            
        backtrace(candidates, [], target, 0)
        return res
