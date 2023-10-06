# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        dic = defaultdict(int)
        dic[0]=1
        ans = 0
        
        def dfs(node,prefixSum):
            nonlocal ans
            if prefixSum - targetSum in dic:
                ans += dic[prefixSum - targetSum]
                
            dic[prefixSum]+=1
            
            if node.left:
                dfs(node.left,prefixSum+node.left.val)
            if node.right:
                dfs(node.right,prefixSum+node.right.val)
                
            dic[prefixSum] -= 1
        
        dfs(root,root.val)
        return ans
