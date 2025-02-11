# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        
        if not t:
            return True
        if not s:
            return false
         
        if sameTree(s,t):
            return True
        return (self.isSubTree(s.left, t) or self.isSubTree(s.right, t))     

        def sameTree(s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if cur.val != subRoot.val:
            return False
        return(self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
        
        
