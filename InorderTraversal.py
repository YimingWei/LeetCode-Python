# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # white表示没有遍历过的节点，gray表示遍历过的
        white = 0
        gray = 1
        stack = [(white, root)]
        res = []
        while stack:
            i, node = stack.pop()
            if node is None: continue
            if i == white:
                # 栈是先进后出，而中序遍历的节点顺序是"左中右"，因此入栈顺序是"右中左"
                stack.extend([(white, node.right), (gray, node), (white, node.left)])
            else:
                res.append(node.val)
        return res
