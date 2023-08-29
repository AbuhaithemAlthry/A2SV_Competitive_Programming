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
        self.first=TreeNode()
        self.mid=TreeNode()
        self.last=TreeNode()
        self.prev=TreeNode(float('-inf'))
        self.first,self.mid,self.last=None,None,None

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            if self.prev!=None and root.val<self.prev.val:
       
                if not self.first:
                    # print('op')
                    self.first=self.prev
                    self.mid=root
                    # print(self.first.val)
                else:
                    self.last=root
            self.prev=root
            inorder(root.right)


        inorder(root)
        if self.first and self.last:
            self.first.val,self.last.val=self.last.val,self.first.val
        elif self.first and self.mid:
            self.first.val,self.mid.val=self.mid.val,self.first.val