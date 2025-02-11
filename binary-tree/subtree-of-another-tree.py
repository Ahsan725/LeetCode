class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False
         
        if self.sameTree(s, t):
            return True
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))  

    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
