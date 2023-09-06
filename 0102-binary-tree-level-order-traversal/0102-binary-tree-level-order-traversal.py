# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            length = len(queue)
            res = []
            while length > 0:
                a = queue.popleft()
                if a:
                    res.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
                length-=1
            ans.append(res)
        return ans