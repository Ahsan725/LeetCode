# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #the main thing to understand here is that it is calling the function itself again as a means to loop through the trees.


        if not p and not q:
            return True #because empty trees are same 
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))