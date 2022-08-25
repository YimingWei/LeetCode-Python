class Solution:
    def numTrees(self, n: int) -> int:
        # 二叉搜索树是指，若左子树不为空则其节点值均小于根节点，若右子树不为空则其节点值均大于根节点
        dp = [0] * (n+1) #因为n=0时，比较特殊，定义此时二叉搜索树种数为1
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
