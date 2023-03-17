class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def recur(root):
            if not root:
                return []
            left=recur(root.left)
            right=recur(root.right)
            return left + [root.val] + right
        res = recur(root)
        return res[k-1]
