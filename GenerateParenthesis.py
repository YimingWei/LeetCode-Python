class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrace(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrace(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrace(S, left, right+1)
                S.pop()
        
        backtrace([], 0, 0)
        return ans
