# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #using DFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lvls = defaultdict(list)  
        def recur(node=root,level=0):
            if not node:
                return
            lvls[level].append(node.val)
            recur(node.left,level+1)
            recur(node.right,level+1)
        recur()
        return [lvls[i][-1] for i in range(len(lvls))]
