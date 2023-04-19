# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path, path_sum):
            if not node:
                return 0

            if not (node.left or node.right):
                num = int("".join(map(str, path)))
                return path_sum + num
            if node.left:
                left_sum = dfs(node.left, path + [node.left.val], path_sum)
            else:
                left_sum = 0
            if node.right:
                right_sum = dfs(node.right, path + [node.right.val], path_sum)
            else:
                right_sum = 0
            return left_sum + right_sum

        if not root:
            return 0

        return dfs(root, [root.val], 0)
