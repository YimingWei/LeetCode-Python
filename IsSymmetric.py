# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right: #left为空right不为空或者left不为空right为空
                return False
            elif left.val != right.val: #left和right都不为空且值不等
                return False
            elif left.val == right.val: #值相等
                return dfs(left.left, right.right) and dfs(left.right, right.left)
        
        return dfs(root.left, root.right)   
