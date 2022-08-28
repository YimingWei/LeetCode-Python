# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, min, max): #要注意保证所有左子树的val小于当前节点val并且小于右子树的val
            if not node:
                return True
            if min and node.val <= min.val:
                return False
            if max and node.val >= max.val:
                return False
            else:
                return check(node.left, min, node) and check(node.right, node, max)
        return check(root, None, None)
