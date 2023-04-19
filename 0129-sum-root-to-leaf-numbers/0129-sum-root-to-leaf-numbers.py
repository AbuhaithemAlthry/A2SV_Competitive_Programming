# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        
        def dfs(node=root, path=[root.val]):
            if not node:
                return
            
            if not (node.left or node.right):
                num = int("".join(map(str, path)))
                paths.append(num)
                
            if node.left:
                path.append(node.left.val)
                dfs(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, path)
                path.pop()
        if not root:
            return 0
        dfs()
        return sum(paths)