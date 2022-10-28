class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.total += root.val
            root.val = self.total
            dfs(root.left)
        
        dfs(root)
        return root
