# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #using DFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = defaultdict(list)

        def listify(node=root, level=0):
            if not node: 
                return
            lvls[level].append(node.val)
            listify(node.left, level+1)
            listify(node.right, level+1)

        listify()
        return [lvls[i] for i in range(len(lvls))]
    # using BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            print([i.val for i in queue])
            temp = []
            for i in range(len(queue)):
                temp.append(queue[i].val)
            
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            ans.append(temp)
        
        return ans
