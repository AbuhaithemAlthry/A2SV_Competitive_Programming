# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def dfs(node=root, res=[root.val]):
            if not node:
                return
            if not (node.left or node.right):
                if sum(res) == targetSum:
                    ans.append(res)
                    return
                return
            if node.left:
                dfs(node.left, res + [node.left.val]) # Fix here
            if node.right:
                dfs(node.right, res + [node.right.val]) # Fix here
        dfs()
        return ans