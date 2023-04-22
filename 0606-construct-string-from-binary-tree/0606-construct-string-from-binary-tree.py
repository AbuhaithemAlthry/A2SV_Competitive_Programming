class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = []
        def dfs(t: TreeNode, res: List[str]) -> None:
            if t is None:
                return
            res.append(str(t.val))
            if t.left is None and t.right is None:
                return
            res.append('(')
            dfs(t.left, res)
            res.append(')')
            if t.right is not None:
                res.append('(')
                dfs(t.right, res)
                res.append(')')
        dfs(t, res)
        return ''.join(res)