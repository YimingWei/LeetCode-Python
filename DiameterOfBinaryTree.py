# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root: return 0
            L = depth(root.left)
            R = depth(root.right)
            self.max = max(self.max, L+R)
            return max(L,R)+1
        self.max = 0
        depth(root)
        return self.max
