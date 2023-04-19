# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = []
        
        def dfs(node=root,path=[root.val]):

            if not (node.left or node.right):
                ans.append(path)
                # path.pop()
                
            if node.left:
                dfs(node.left,path+[node.left.val])
            if node.right:
                dfs(node.right,path+[node.right.val])
            
            return path
        
        dfs()
        
        _sum_=0
        for i in range(len(ans)):
            _sum_ += int("".join(map(str, ans[i])))

        return _sum_