# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        
        max_width = 1
        queue = deque([(root, 0)])

        while queue:
            n = len(queue)
            leftIndex = inf
            rightIndex = -inf
            for _ in range(n):
                node, index = queue.popleft()
                leftIndex = min(leftIndex, index)
                rightIndex = max(rightIndex, index)

                if node.left:
                    queue.append((node.left, 2 * index))
                
                if node.right:
                    queue.append((node.right, 2 * index +1))
                
            max_width = max(max_width, rightIndex - leftIndex + 1)
        return max_width 