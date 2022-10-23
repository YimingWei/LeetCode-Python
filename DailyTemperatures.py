class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # 1.暴力（时间超时）
        # res = []
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res.append(j-i)
        #             break
        #         elif temperatures[j] <= temperatures[i] and j == n-1:
        #             res.append(0)
        # res.append(0)
        # return res
        # 2.单调栈
        res = [0] * n
        stack = []
        for i, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res
