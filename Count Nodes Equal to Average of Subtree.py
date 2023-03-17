# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(node):
            nonlocal res
            if not node:
                return (0,0)
            
            left_sum, left_co = recur(node.left)
            right_sum, right_co = recur(node.right)

            s = node.val + left_sum + right_sum
            c = 1 + left_co + right_co

            if (s//c)==node.val:
                res+=1
                
            return s,c
            
        recur(root)
        return res
            
