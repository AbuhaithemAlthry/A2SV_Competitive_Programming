# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #using BFS 
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = defaultdict(list)
        def recur(node=root,x=0,y=0):
            if not node:
                return
            lvls[x].append((y,node.val))
            recur(node.right,x+1,y+1)
            recur(node.left,x-1,y+1)
        recur()
        res=[]
        #since tuple compare two values based on the first element and if the fist elements are equal they compare based on the second element
        for x in sorted(lvls.keys()):
            res.append([tup[1] for tup in sorted(lvls[x])])
        return res
