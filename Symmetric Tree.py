# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(l_root,r_root):
            if not l_root and not r_root:
                return True
            if (not l_root or not r_root) or l_root.val != r_root.val:
                return False
            return compare(l_root.left,r_root.right) and compare(r_root.left,l_root.right)
        res = compare(root.left,root.right)
        return res
