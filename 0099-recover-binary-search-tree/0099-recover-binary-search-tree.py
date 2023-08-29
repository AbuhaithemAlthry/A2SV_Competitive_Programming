# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def inOrder(node):
            if not node:
                return 
            inOrder(node.left)
            arr.append(node)
            inOrder(node.right)
            return 

        inOrder(root)
        sortedArr = sorted(arr, key=lambda x:x.val)
        for i in range(len(arr)):
            if arr[i].val != sortedArr[i].val:
                arr[i].val, sortedArr[i].val = sortedArr[i].val, arr[i].val
                return