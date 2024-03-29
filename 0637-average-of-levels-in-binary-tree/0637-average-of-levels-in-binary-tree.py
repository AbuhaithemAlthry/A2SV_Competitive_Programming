# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        queue = [root]
        levelOrder = []

        while queue:
            cur_level = []
            length = len(queue)

            while length > 0:
                cur = queue.pop(0)
                cur_level.append(cur.val)
                length -= 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            levelOrder.append(sum(cur_level)/len(cur_level))

        return levelOrder