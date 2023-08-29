# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return 0,None
            hl,lcal= dfs(node.left)
            hr,lcar= dfs(node.right)
            if hl>hr:
                return hl+1,lcal
            if hl<hr:
                return hr+1,lcar
            return hl+1,node
        
        return dfs(root)[1]