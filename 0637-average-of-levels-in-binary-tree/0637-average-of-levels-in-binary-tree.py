# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        levels = deque([root])
        while levels:
            sum_level, level = 0, 0
            temp = deque()
            while levels:
                node = levels.popleft()
                sum_level += node.val
                level += 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            levels = temp
            res.append(sum_level / level)
        return res

            