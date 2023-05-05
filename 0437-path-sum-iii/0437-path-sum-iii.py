# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0
    
        def recur(node,pre_sum):
            nonlocal ans
            if not node:
                return
            
            pre_sum += node.val

            if pre_sum - targetSum in dic:
                ans += dic[pre_sum - targetSum]
            
            dic[pre_sum] += 1


            recur(node.left,pre_sum)

            recur(node.right,pre_sum)

            dic[pre_sum]-=1

        recur(root,0)
        
        return ans