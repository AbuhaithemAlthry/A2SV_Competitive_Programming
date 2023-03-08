# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(cur_root,p,q):
            if p.val > cur_root.val and q.val > cur_root.val:
                return recur(cur_root.right,p,q)
            elif p.val < cur_root.val and q.val < cur_root.val:
                return recur(cur_root.left,p,q)
            else:
                return cur_root
        res = recur(root,p,q)
        return res
