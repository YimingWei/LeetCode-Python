class Solution:
    def countBits(self, n: int) -> List[int]:
        # 1.递归
        # dp = [0] * (n+1)
        # def recursion(k):
        #     if k == 0:
        #         return 0
        #     elif k % 2 == 0:
        #         return recursion(k/2)
        #     else:
        #         return recursion(k-1)+1
        # for i in range(n+1):
        #     dp[i] = recursion(i)
        # return dp
        # 2.迭代
        res = [0]
        for i in range(1, n+1):
            if i % 2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[-1]+1)
        return res
