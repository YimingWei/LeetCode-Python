# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = [root] if root else []
        while stack:
            next_node = []
            res.append([node.val for node in stack])
            for node in stack:
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            stack = next_node
        return res
